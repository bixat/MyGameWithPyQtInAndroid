#بسم الله الرحمان الرحيم و الحمد لله رب العالمين على نعمه التي لا تعد و لاتحصى ربي زدنا علما وإنفعنا بما علمتنا و إنفع بنا غيرنا و إرزقنا الأجر 
#هذا من فضل ربي
#محمد شهبون
#fb.com/chahboun2
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import random
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setStyleSheet("background-color: rgb(25,25,65)")
    global b, lb, lbl
    lbl = []
    for i in range(4):
    	lb = QLabel(w)
    	lbl.append(lb)
    lbl[0].setText('Points : 6/0')
    lbl[0].setGeometry(10,0,800,150)
    lbl[0].setFont(QFont("Time", 20, QFont.Bold))
    lbl[0].setStyleSheet("color: rgb(50,75,250);")
    lbl[1].setStyleSheet("background-color: rgb(50,76,250); color: rgb(25,25,65);")
    lbl[1].setGeometry(10,150,800,150)
    lbl[2].setStyleSheet("background-color: rgb(50,75,250);")
    lbl[2].setText('My Game')
    lbl[2].setFont(QFont("Times", 40, QFont.Bold))
    lbl[2].setGeometry(280,150,800,150)
    bs = QPushButton(w)
    bs.setText('Start')
    bs.setStyleSheet("background-color: rgb(25,25,65); color: rgb(255,255,255);")
    bs.setFont(QFont("Times", 25, QFont.Bold))
    bs.setGeometry(340,1600,400,150)
    m =0
    l = 0
    b = []
    for i in range(12):
    	t = QPushButton(w)
    	t.setFont(QFont("Times", 40, QFont.Bold))
    	t.setEnabled(False)
    	b.append(t)
    	t.setGeometry(140+l, 400+m, 200, 200)
    	m += 300
    	if m == 1200:
    		m=0
    		l +=300
    bs.clicked.connect(start)
    for i in range(12):
    	fun = 'bt'+str(i)
    	b[i].clicked.connect(eval(fun))
    global v,a
    v = []
    a = ['●', '♡','♤','■','□','♧']
    for i in b:
    	c = random.choice(a)
    	i.setText(c)
    	i.setFont(QFont("Times", 20, QFont.Bold))
    	v.append(c)
    	if v.count(c) == 2:
    		a.remove(c)
    w.show()
    sys.exit(app.exec_())
def start():
	global bc
	for i in b:
		i.setText('')
		i.setEnabled(True)
		i.setStyleSheet("background-color: rgb(25,25,65); color: rgb(0,0,0);")
		bc = [-1]
		lbl[2].setText("My Game")
def bt0():
	ai(0)
def bt1():
	ai(1)
def bt2():
	ai(2)
def bt3():
	ai(3)
def bt4():
	ai(4)
def bt5():
	ai(5)
def bt6():
	ai(6)
def bt7():
	ai(7)
def bt8():
	ai(8)
def bt9():
	ai(9)
def bt10():
	ai(10)
def bt11():
	ai(11)
global p, e
p = 0
e = 0
f = [42,84,126,168,210,250]
def ai(n):
	global p, f, e
	b[n].setText(v[n])
	b[n].setStyleSheet("color: rgb(255,255,255);")
	try:
		if bc[-1] == n:
			bc.pop()
	except IndexError:
		b[0].setText("hello")
	if v[n] == v[bc[-1]]:
		b[n].setText(v[n])
		b[bc[-1]].setText(v[bc[-1]])
		p += 1
		lbl[0].setText('Points : 6/{}'.format(p))
		c = random.choice(f)
		b[n].setStyleSheet("background-color: rgb({0},126,25); color: rgb(0,{0},{1});".format(c, c/2))
		b[bc[-1]].setStyleSheet("background-color: rgb({0},126,25); color: rgb(0,{0},{1});".format(c, c/2))
		f.remove(c)
		b[n].setFont(QFont("Times", 40, QFont.Bold))
		b[bc[-1]].setFont(QFont("Times", 40, QFont.Bold))
		b[n].setEnabled(False)
		b[bc[-1]].setEnabled(False)
	elif v[n] != v[bc[-1]]:
		b[n].setText(v[n])
		QTimer.singleShot(1000, lambda:b[n].setText(''))
	bc.append(n)
	if p == 6:
		lbl[2].setText("Good Job !")
		bc.clear()
		bc.append(-1)
		p = 0
if __name__ == '__main__':
	window()
