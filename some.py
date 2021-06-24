import os
os.system('pip install keyboard')
import keyboard as keyb

evs=['0','1','2','3','4','5','6','7','8','9']
num=''
nums=''
def eventer(event):
    global num,nums
    if isinstance(event, keyb.KeyboardEvent):
        if event.name in evs and event.event_type=='down':
            if keyb.is_pressed('tab'):
                num+=str(evs.index(event.name))
                keyb.press('backspace')
            elif keyb.is_pressed('ctrl'): nums+=str(evs.index(event.name))
        elif num!='' and event.name=='tab' and event.event_type=='down': num=''
        elif nums!='' and event.name=='ctrl' and event.event_type=='down': nums=''
        elif event.name=='`' and event.event_type=='down' and keyb.is_pressed('ctrl'):
            zz=''
            for i in range(len(spz[int(num)-1])): zz+=(spz[int(num)-1][i]+'\n')
            f=open('x'+num+'.py','w',encoding='UTF-8')
            f.write(zz)
            f.close()
        elif nums!='' and event.name=='ctrl' and event.event_type=='up':
            keyb.write(spz[int(num)-1][int(nums)-1]+'\n')
            keyb.press('home')
        elif event.name=='esc' and event.event_type=='down': exit()

spz=[]
spz+=['''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self): super().__init__()
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        pen = QPen()
        qp.setPen(pen)
        brush = QBrush(Qt.BDiagPattern)
        brush.setColor(QColor(255, 255, 0))
        qp.setBrush(brush)
        qp.drawRoundedRect(20, 20 ,150, 100, 15, 15)
        qp.end()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w=Example()
    w.show()
    app.exec_()
''']
spz+=['''
import pygame
class Obj(pygame.sprite.Sprite):
    def __init__(self,typ,x,y,pic):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pic)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.nap,self.typ=5,typ
    def update(self):
        if self.typ==0: return
        self.rect.x += self.nap
        if self.rect.left > 750: self.nap=-5
        elif self.rect.right < 50: self.nap=5
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Obj(0,50,300,'k.png')
player2 = Obj(0,750,300,'k2.png')
ball = Obj(1,100,300,'b.png')
all_sprites.add(player,player2,ball)
while True:
    clock.tick(60)
    all_sprites.update()
    screen.fill((255,255,255))
    all_sprites.draw(screen)
    pygame.display.flip()
''']
spz+=['''
import sys # Импорт модулей
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Button(QPushButton): # класс кнопки
    def __init__(self, title, parent): super().__init__(title, parent)
    def mouseMoveEvent(self, e): #
        mimeData = QMimeData()
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos()-self.rect().topLeft())
        dropAction = drag.exec_(Qt.MoveAction)
class Example(QWidget): # создание окна
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.btns=[0,0,0,0,0,0] # создание кнопок
        for i in range(6):
            self.btns[i] = Button('Button'+str(i), self)
            self.btns[i].enterEvent = lambda x,i=i: self.gett(i)
            self.btns[i].move(10+i*90, 10)
    def dragEnterEvent(self, e):e.accept() # начало перемещения
    def gett(self,i): self.j=i # запоминание перемещаемой кнопки
    def dropEvent(self, e): # изменение координат кнопки при отпускании
        self.btns[self.j].move(e.pos())
        e.setDropAction(Qt.MoveAction)
        e.accept()
if __name__ == '__main__': # Запуск окна
    app=QApplication(sys.argv)
    w=Example()
    w.show()
    app.exec_()
''']
spz+=['''
from PyQt5.QtWidgets import * # Импорт модулей
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3,sys

conn = sqlite3.connect("shop.db") # Чтение из базы
cursor = conn.cursor()
data=cursor.execute("select * from things").fetchall()
class Example(QMainWindow): # Создание окна
    def __init__(self):
        super().__init__()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
        self.table = QTableWidget(self) # Создание таблицы
        self.table.setColumnCount(3)
        self.table.setRowCount(len(data))
        self.table.setHorizontalHeaderLabels(["Товар", "Цена", "Кол-во"])
        for i in range(len(data)): # Заполнение таблицы
            for j in range(3): self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        self.table.resizeColumnsToContents()
        self.table.cellChanged.connect(lambda x: self.chdata()) # Изменение итога при изменении ячейки
        grid_layout.addWidget(self.table, 0, 0)
        self.la = QLabel() # Создание лейбла
        self.la.setText("Общая сумма: 0")
        self.la.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(self.la, 1, 0)
    def chdata(self,itog=0): # Функция записи итога в лейбл
        for i in range(len(data)): itog+=int(self.table.item(i,1).text())*int(self.table.item(i,2).text())
        self.la.setText("Общая сумма: "+str(itog))
if __name__ == '__main__': # запуск приложения
    app = QApplication(sys.argv)
    w=Example()
    w.show()
    app.exec_()
''']
spz+=['''
from PyQt5.QtWidgets import * # Импорт модулей
import sys

class Example(QWidget): # Создание окна
    def __init__(self):
        super().__init__()
        layout = QGridLayout() # Создание сетки для расположения виджетов 
        self.setLayout(layout)
        ls=[['Как относишься к PyQt?','плохо','нейтрально','отлично','#12 из 10'],
            ['PyQt - лучшее изобретение человечества?','да','нет','#разве есть сомнения?','возможно'],
            ['Есть что-либо лучше PyQt?','да','да','#нет','да']]
        self.rezs=[0,0,0] # для хранения ответов на вопросы
        for j in range(3): # Создание циклом лейблов и радиокнопок
            l1 = QLabel(ls[j][0])
            layout.addWidget(l1, j*5, 0)
            group=QButtonGroup(self) # Сбор кнопок одного вопроса в группу
            for i in range(4): # Создание радиокнопок 
                rbs = QRadioButton(ls[j][i+1].replace('#',''))
                rbs.count = [ls[j][i+1][0],j] # count(можно любое имя) - привязанная к кнопке переменная для хранения любой инфы   
                rbs.toggled.connect(self.onClicked)
                group.addButton(rbs)
                layout.addWidget(rbs, j*5+i+1, 0)
        button = QPushButton("Завершить")
        button.clicked.connect(self.rez)
        layout.addWidget(button, j*5+i+2, 0)
    def onClicked(self): # при клике по радиокнопке с помощью self.sender() обращаемся к переменной count и изменяем результаты теста
        if self.sender().count[0]=='#': self.rezs[self.sender().count[1]]=1
        else: self.rezs[self.sender().count[1]]=0
    def rez(self): # Считываем результаты и блокируем тест
        self.setEnabled(False) 
        dlg = QDialog(self)
        dlg.layout = QVBoxLayout()
        message = QLabel("Тест завершен!\nРезультат: "+str(self.rezs.count(1)+2))
        dlg.layout.addWidget(message)
        dlg.setLayout(dlg.layout)
        dlg.exec()
if __name__ == "__main__": # Запуск окна
    app = QApplication(sys.argv)
    w=Example()
    w.show()
    app.exec_()
''']
spz+=['''
from PyQt5.QtWidgets import * # Импорт модулей
from PyQt5.QtGui import *
import sys

class Example(QMainWindow): # Создание окна программы
    def __init__(self):
        super().__init__()
        menuBar = self.menuBar()
        Men = QMenu("Dialogs", self)
        menuBar.addMenu(Men)
        bnames=['Input Dialog','Color Dialog','Font Dialog','File Dialog','Custom Dialog']
        for i in range(5): # Создание пунктов меню циклом, чтоб короче было
            act = QAction(bnames[i], self)
            Men.addAction(act)
            act.triggered.connect(eval('self.showDialog'+str(i)))
    def showDialog0(self): # Диалог ввода
        text,ok = QInputDialog.getText(self, 'Input Dialog','Enter text:')
        if ok: print(str(text))
    def showDialog1(self): # Диалог цвета
        col = QColorDialog.getColor()
        print(col.name())
    def showDialog2(self): # Диалог шрифта
        font, ok = QFontDialog.getFont()
        if ok: print(font.family(),font.weight())
    def showDialog3(self): # Диалог файлов
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        f = open(fname, 'r')
        print(f.read())
    def showDialog4(self): # Настраиваемый диалог (как обычное окно)
        dlg = QDialog(self)
        dlg.layout = QVBoxLayout()
        message = QLabel("Text\nVery some text")
        dlg.layout.addWidget(message)
        dlg.setLayout(dlg.layout)
        dlg.exec()
if __name__ == '__main__': # Запуск окна
    app = QApplication(sys.argv)
    w=Example()
    w.show()
    sys.exit(app.exec_())
''']
spz+=['''
from PyQt5.QtWidgets import * # Импорт модулей
from PyQt5.QtCore import *
import sqlite3,sys

conn = sqlite3.connect("sotrud.db") # Чтение из базы
cursor = conn.cursor()
data=cursor.execute("select * from sotruds").fetchall()
class Example(QMainWindow): # Создание окна
    def __init__(self):
        super().__init__()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
        self.table = QTableWidget(self) # Создание таблицы
        self.table.setColumnCount(11)
        self.table.setRowCount(len(data))
        self.table.setHorizontalHeaderLabels(["Таб.номер", "Фамилия", "Дата рожд.","Профессия","Подр.","Дата приема","Дата нач.тр.д.","Оклад","Образ.","Спец.","Должность"])
        for i in range(len(data)): # Заполнение таблицы
            for j in range(11): self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        self.table.resizeColumnsToContents()
        grid_layout.addWidget(self.table, 0, 0)
        self.qle = QLineEdit(self) # Создание поля ввода
        grid_layout.addWidget(self.qle, 1, 0)
        self.btn = QPushButton('Найти фамилию', self) # Создание кнопки
        grid_layout.addWidget(self.btn, 2, 0)
        self.btn.clicked.connect(self.search)
    def search(self,ii=0):
        self.table.setRowCount(0) # Очистка таблицы
        self.table.setRowCount(len(data))
        for i in range(len(data)): # Заполнение таблицы
            if data[i][1]==self.qle.text() or self.qle.text()=='':
                for j in range(11): self.table.setItem(ii, j, QTableWidgetItem(str(data[i][j])))
                ii+=1
if __name__ == "__main__": # Создание окна
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    app.exec_()
''']
spz+=['''
from PyQt5.QtWidgets import * # Импорт модулей
from PyQt5.QtGui import *
import sys

class Example(QWidget): # Создание окна программы
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,170,200)
        self.msg = QLabel(self)
        self.msg.setText("Введите кол-во букв в слове:")
        self.msg.move(10, 10)
        self.qle = QLineEdit(self) # Создание поля ввода
        self.qle.move(10, 40)
        self.btn = QPushButton('Выберите файл', self) # Создание кнопки
        self.btn.clicked.connect(self.showDialog)
        self.btn.move(10, 70)
        self.msg2 = QLabel(self) # Лейбл для записи результата
        self.msg2.setText("Искомое слово:                                ")
        self.msg2.move(10, 100)
    def showDialog(self): # Диалог файлов
        try:
            int(self.qle.text()) # проверка ввода и открытие файла
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            f = open(fname, 'r')
        except: return
        tx=f.read().replace('\n',' ').split(' ') # перевод текста в список слов
        for i in range(len(tx)): # Проход по списку и поиск совпадений
            if len(tx[i])==int(self.qle.text()):
                self.msg2.setText("Искомое слово: "+tx[i])
                break
if __name__ == '__main__': # Запуск окна
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    app.exec_()
''']
spz+=['''
from PyQt5.QtWidgets import * # Импорт модулей
from PyQt5.QtCore import *
from PyQt5.Qt import *
from datetime import datetime
import sys

class Example(QMainWindow): # Создание окна программы
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,280,300)
        self.qle = QPlainTextEdit(self) # Создание поля ввода
        self.qle.setGeometry(QRect(10, 50, 260, 220))
        self.btn = QPushButton('Выберите файл', self) # Создание кнопки
        self.btn.clicked.connect(self.showDialog)
        self.btn.move(10, 10)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.chstbar)
        self.timer.start()
    def showDialog(self): # Диалог файлов
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        f = open(fname, 'r')
        self.qle.clear()
        self.qle.setPlainText(f.read())
    def chstbar(self):
        self.statusBar().showMessage(datetime.today().strftime("%m.%d.%Y %H:%M:%S"))
if __name__ == '__main__': # Запуск окна
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(app.exec_())
''']
spz+=['''
import pygame # импорт модулей
import math
from random import randint as ra

wx = 800 # ширина окна
wy = 600 # высота окна
acc=1 # Точность
kl=10 # Размер одной единицы в пикселях
grap=['-3/x','-3/x+1'] # графики

pygame.init() # создание окна
screen = pygame.display.set_mode([wx,wy],pygame.FULLSCREEN)
mx,my=wx//2,wy//2, # определение середины окна
pygame.draw.line(screen,[255,255,255],[0,my],[wx,my])
pygame.draw.line(screen,[255,255,255],[mx,0],[mx,wy])
for i in range(len(grap)): # создание графиков
    spt=[] # точки
    col=[ra(50,255),ra(50,255),ra(50,255)] # цвет
    for x in range(-mx,mx,acc):
        try: y=eval(grap[i].replace('x',str(x/kl)))*kl # взятие графика из списка и замена "х" на значение
        except: continue
        spt+=[[x+mx,y+my]]
        if len(spt)>2: # прорисовка графика
            pygame.draw.lines(screen,col,0,spt)
            pygame.time.delay(5)
            pygame.display.flip()
pygame.time.delay(2000)
pygame.quit()
''']
spz+=['''
from PyQt5.QtWidgets import * # Импорт модулей
from PyQt5.QtCore import *
from PyQt5.Qt import *
from xml.dom import minidom
import sys

class Example(QMainWindow): # Создание окна программы
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,280,300)
        self.qle = QPlainTextEdit(self) # Создание поля ввода
        self.qle.setGeometry(QRect(10, 50, 260, 220))
        self.btn = QPushButton('Выберите xml', self) # Создание кнопки
        self.btn.clicked.connect(self.showDialog)
        self.btn.move(10, 10)
    def showDialog(self): # Диалог файлов
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.qle.clear()
        
        self.dom = minidom.parse(fname)
        self.collection = self.dom.documentElement
        self.linesArr = self.collection.getElementsByTagName('text')
        for line in self.linesArr: # Вывод текста из тега и текста между <text></text>
            self.qle.appendPlainText(line.getAttribute('what'))
            self.qle.appendPlainText(line.childNodes[0].data)
if __name__ == '__main__': # Запуск окна
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    app.exec_()
''']
spz+=['''
from PyQt5.QtWidgets import * # Импорт модулей
import sys

def bank(x,y): # Функция рассчета итоговой суммы
    for i in range(y): x=x*1.1
    return round(x,5)
class Example(QWidget): # Создание окна программы
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,220,200)
        self.msg = QLabel(self)
        self.msg.setText("Введите размер вклада и кол-во лет:")
        self.msg.move(10, 10)
        self.qle = QLineEdit(self) # Создание поля ввода
        self.qle.move(10, 40)
        self.qle2 = QLineEdit(self)
        self.qle2.move(10, 70)
        self.btn = QPushButton('Рассчитать', self) # Создание кнопки
        self.btn.clicked.connect(self.banker)
        self.btn.move(10, 100)
        self.msg2 = QLabel(self) # Лейбл для записи результата
        self.msg2.setText("Итоговая сумма:                                ")
        self.msg2.move(10, 130)
    def banker(self): # Cбор и вывод информации
        try: x,y=int(self.qle.text()),int(self.qle2.text())
        except: return
        self.msg2.setText("Итоговая сумма: "+str(bank(x,y)))
if __name__ == '__main__': # Запуск окна
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    app.exec_()
''']
spz+=['''
from PyQt5.QtWidgets import * # Импорт модулей
import sys
from random import randint as ra

class Example(QWidget): # Создание окна программы
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,300,100)
        self.msg = QLabel(self)
        self.sp=[ra(-50,50) for i in range(10)] # Создание списка
        self.msg.setText("Список: "+str(self.sp))
        self.msg.move(10, 10)
        self.btn = QPushButton('Рассчитать', self) # Создание кнопки
        self.btn.clicked.connect(self.counter)
        self.btn.move(10, 40)
        self.msg2 = QLabel(self) # Лейбл для записи результата
        self.msg2.setText("Сумма пол. элементов:                ")
        self.msg2.move(10, 70)
    def counter(self): # Рассчет
        self.msg2.setText("Сумма пол. элементов: "+str(sum([i for i in self.sp if i>0])))
if __name__ == '__main__': # Запуск окна
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    app.exec_()
''']
for i in range(len(spz)): spz[i]=spz[i].split('\n')
keyb.hook(eventer)
