#!/usr/bin/python3
# BU PROGRAM GÖKSEL GÜRSU TARAFINDAN YAPILMIŞTIR.

from tkinter import *
import pygame
import time
import random

pygame.mixer.init()

pencere=Tk()
pencere.tk_setPalette("white")
pencere.attributes("-fullscreen", 1)
       
Label2=Label(text="1'den 20'ye kadar sayıları sırayla hızlı bir şekilde butonlara basarak tamamlayınız.",font="TTKBDikTemelAbece 12")
Label2.place(relx = 0.01, rely = 0.92)

Label4=Label(text="DİKKAT ARTTIRMA OYUNU",font="TTKBDikTemelAbece 20")
Label4.place(relx = 0.40, rely = 0.02)

label=Label(text="gokselgursu@gmail.com --- http://www.egitimhane.com/",font="TTKBDikTemelAbece 12")
label.place(relx = 0.74, rely = 0.95)

xy=[["0.08","0.1"],["0.16","0.1"],["0.24","0.1"],["0.32","0.1"],["0.4","0.1"],["0.48","0.1"],["0.56","0.1"],["0.64","0.1"],["0.72","0.1"],["0.8","0.1"],["0.88","0.1"], \
    ["0.08","0.2"],["0.16","0.2"],["0.24","0.2"],["0.32","0.2"],["0.4","0.2"],["0.48","0.2"],["0.56","0.2"],["0.64","0.2"],["0.72","0.2"],["0.8","0.2"],["0.88","0.2"], \
    ["0.08","0.3"],["0.16","0.3"],["0.24","0.3"],["0.32","0.3"],["0.4","0.3"],["0.48","0.3"],["0.56","0.3"],["0.64","0.3"],["0.72","0.3"],["0.8","0.3"],["0.88","0.3"], \
    ["0.08","0.4"],["0.16","0.4"],["0.24","0.4"],["0.32","0.4"],["0.4","0.4"],["0.48","0.4"],["0.56","0.4"],["0.64","0.4"],["0.72","0.4"],["0.8","0.4"],["0.88","0.4"], \
    ["0.08","0.5"],["0.16","0.5"],["0.24","0.5"],["0.32","0.5"],["0.4","0.5"],["0.48","0.5"],["0.56","0.5"],["0.64","0.5"],["0.72","0.5"],["0.8","0.5"],["0.88","0.5"], \
    ["0.08","0.6"],["0.16","0.6"],["0.24","0.6"],["0.32","0.6"],["0.4","0.6"],["0.48","0.6"],["0.56","0.6"],["0.64","0.6"],["0.72","0.6"],["0.8","0.6"],["0.88","0.6"], \
    ["0.08","0.7"],["0.16","0.7"],["0.24","0.7"],["0.32","0.7"],["0.4","0.7"],["0.48","0.7"],["0.56","0.7"],["0.64","0.7"],["0.72","0.7"],["0.8","0.7"],["0.88","0.7"], \
    ["0.08","0.8"],["0.16","0.8"],["0.24","0.8"],["0.32","0.8"],["0.4","0.8"],["0.48","0.8"],["0.56","0.8"],["0.64","0.8"],["0.72","0.8"],["0.8","0.8"],["0.88","0.8"]]
    
e=[]
e1=[]
e2=[]
e3=[]
e4=[]
e5=[]
e6=[]
e7=[]
e8=[]
e9=[]
e10=[]
e11=[]
e12=[]
e13=[]
e14=[]
e15=[]
e16=[]
e17=[]
e18=[]
e19=[]



def aşama20():
    import time
    global toplam1,e19,e18,e17,e16,e15,e14,e13,e12,e11,e10,e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    pygame.mixer.music.load("alkis.ogg")
    pygame.mixer.music.play()

    time.sleep(3)

    time22 = time.strftime("%H:%M:%S")
    time2 = time.strftime("%H %M %S")

    sonu1=Label(text="Oyunu Bitiriş Zamanı     "+time22,font="TTKBDikTemelAbece 16")
    sonu1.place(relx = 0.4, rely = 0.91)

    zaman2=time2.split()
    saat2=int(zaman2[0])*3600
    dakika2=int(zaman2[1])*60
    saniye2=int(zaman2[2])
    toplam2=saat2+dakika2+saniye2

    zamanfark=int(toplam2 - toplam1)
    saatler=zamanfark//3600
    dakikalar=zamanfark%3600//60
    saniyeler=zamanfark%60

    sonu2=Label(text="Geçen Süre                "+str(saatler)+":"+str(dakikalar)+":"+str(saniyeler),font="TTKBDikTemelAbece 16")
    sonu2.place(relx = 0.4, rely = 0.96)
        
    pygame.mixer.music.load("fon.ogg")
    pygame.mixer.music.play(-1)

    h19=e19[0][0]
    t19=e19[0][1]
    
    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama19():
    global e18,e17,e16,e15,e14,e13,e12,e11,e10,e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    h18=e18[0][0]
    t18=e18[0][1]

    e18.remove(e18[0])

    for d in random.sample((e18),1):
        e19.append(d)
        e18.remove(d)

    h19=e19[0][0]
    t19=e19[0][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",command=aşama20,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama18():
    global e17,e16,e15,e14,e13,e12,e11,e10,e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    h17=e17[0][0]
    t17=e17[0][1]

    e17.remove(e17[0])

    q=0

    while q<2:
        for d in random.sample((e17),1):
            e18.append(d)
            e17.remove(d)
            q+=1

            break

    h18=e18[0][0]
    t18=e18[0][1]

    h19=e18[1][0]
    t19=e18[1][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",command=aşama19,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama17():
    global e16,e15,e14,e13,e12,e11,e10,e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    h16=e16[0][0]
    t16=e16[0][1]

    e16.remove(e16[0])

    q=0

    while q<3:
        for d in random.sample((e16),1):
            e17.append(d)
            e16.remove(d)
            q+=1

            break

    h17=e17[0][0]
    t17=e17[0][1]

    h18=e17[1][0]
    t18=e17[1][1]

    h19=e17[2][0]
    t19=e17[2][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",command=aşama18,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama16():
    global e15,e14,e13,e12,e11,e10,e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    h15=e15[0][0]
    t15=e15[0][1]

    e15.remove(e15[0])

    q=0

    while q<4:
        for d in random.sample((e15),1):
            e16.append(d)
            e15.remove(d)
            q+=1

            break

    h16=e16[0][0]
    t16=e16[0][1]

    h17=e16[1][0]
    t17=e16[1][1]

    h18=e16[2][0]
    t18=e16[2][1]

    h19=e16[3][0]
    t19=e16[3][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",command=aşama17,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama15():
    global e14,e13,e12,e11,e10,e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    h14=e14[0][0]
    t14=e14[0][1]

    e14.remove(e14[0])

    q=0

    while q<5:
        for d in random.sample((e14),1):
            e15.append(d)
            e14.remove(d)
            q+=1

            break

    h15=e15[0][0]
    t15=e15[0][1]

    h16=e15[1][0]
    t16=e15[1][1]

    h17=e15[2][0]
    t17=e15[2][1]

    h18=e15[3][0]
    t18=e15[3][1]

    h19=e15[4][0]
    t19=e15[4][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",command=aşama16,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama14():
    global e13,e12,e11,e10,e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    h13=e13[0][0]
    t13=e13[0][1]

    e13.remove(e13[0])

    q=0

    while q<6:
        for d in random.sample((e13),1):
            e14.append(d)
            e13.remove(d)
            q+=1

            break

    h14=e14[0][0]
    t14=e14[0][1]

    h15=e14[1][0]
    t15=e14[1][1]

    h16=e14[2][0]
    t16=e14[2][1]

    h17=e14[3][0]
    t17=e14[3][1]

    h18=e14[4][0]
    t18=e14[4][1]

    h19=e14[5][0]
    t19=e14[5][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",command=aşama15,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama13():
    global e12,e11,e10,e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    h12=e12[0][0]
    t12=e12[0][1]
    
    e12.remove(e12[0])

    q=0

    while q<7:
        for d in random.sample((e12),1):
            e13.append(d)
            e12.remove(d)
            q+=1

            break

    h13=e13[0][0]
    t13=e13[0][1]

    h14=e13[1][0]
    t14=e13[1][1]

    h15=e13[2][0]
    t15=e13[2][1]

    h16=e13[3][0]
    t16=e13[3][1]

    h17=e13[4][0]
    t17=e13[4][1]

    h18=e13[5][0]
    t18=e13[5][1]

    h19=e13[6][0]
    t19=e13[6][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",command=aşama14,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama12():
    global e11,e10,e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    h11=e11[0][0]
    t11=e11[0][1]

    
    e11.remove(e11[0])

    q=0

    while q<8:
        for d in random.sample((e11),1):
            e12.append(d)
            e11.remove(d)
            q+=1

            break

    h12=e12[0][0]
    t12=e12[0][1]

    h13=e12[1][0]
    t13=e12[1][1]

    h14=e12[2][0]
    t14=e12[2][1]

    h15=e12[3][0]
    t15=e12[3][1]

    h16=e12[4][0]
    t16=e12[4][1]

    h17=e12[5][0]
    t17=e12[5][1]

    h18=e12[6][0]
    t18=e12[6][1]

    h19=e12[7][0]
    t19=e12[7][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",command=aşama13,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama11():
    global e10,e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    h10=e10[0][0]
    t10=e10[0][1]

    
    e10.remove(e10[0])

    q=0

    while q<9:
        for d in random.sample((e10),1):
            e11.append(d)
            e10.remove(d)
            q+=1

            break

    h11=e11[0][0]
    t11=e11[0][1]

    h12=e11[1][0]
    t12=e11[1][1]

    h13=e11[2][0]
    t13=e11[2][1]

    h14=e11[3][0]
    t14=e11[3][1]

    h15=e11[4][0]
    t15=e11[4][1]

    h16=e11[5][0]
    t16=e11[5][1]

    h17=e11[6][0]
    t17=e11[6][1]

    h18=e11[7][0]
    t18=e11[7][1]

    h19=e11[8][0]
    t19=e11[8][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",command=aşama12,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama10():
    global e9,e8,e7,e6,e5,e4,e3,e2,e1,e

    h9=e9[0][0]
    t9=e9[0][1]

    
    e9.remove(e9[0])

    q=0

    while q<10:
        for d in random.sample((e9),1):
            e10.append(d)
            e9.remove(d)
            q+=1

            break

    h10=e10[0][0]
    t10=e10[0][1]

    h11=e10[1][0]
    t11=e10[1][1]

    h12=e10[2][0]
    t12=e10[2][1]

    h13=e10[3][0]
    t13=e10[3][1]

    h14=e10[4][0]
    t14=e10[4][1]

    h15=e10[5][0]
    t15=e10[5][1]

    h16=e10[6][0]
    t16=e10[6][1]

    h17=e10[7][0]
    t17=e10[7][1]

    h18=e10[8][0]
    t18=e10[8][1]

    h19=e10[9][0]
    t19=e10[9][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",command=aşama11,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama9():
    global e8,e7,e6,e5,e4,e3,e2,e1,e

    h8=e8[0][0]
    t8=e8[0][1]

    
    e8.remove(e8[0])

    q=0

    while q<11:
        for d in random.sample((e8),1):
            e9.append(d)
            e8.remove(d)
            q+=1

            break

    h9=e9[0][0]
    t9=e9[0][1]

    h10=e9[1][0]
    t10=e9[1][1]

    h11=e9[2][0]
    t11=e9[2][1]

    h12=e9[3][0]
    t12=e9[3][1]

    h13=e9[4][0]
    t13=e9[4][1]

    h14=e9[5][0]
    t14=e9[5][1]

    h15=e9[6][0]
    t15=e9[6][1]

    h16=e9[7][0]
    t16=e9[7][1]

    h17=e9[8][0]
    t17=e9[8][1]

    h18=e9[9][0]
    t18=e9[9][1]

    h19=e9[10][0]
    t19=e9[10][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",command=aşama10,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama8():
    global e7,e6,e5,e4,e3,e2,e1,e

    h7=e7[0][0]
    t7=e7[0][1]

    
    e7.remove(e7[0])

    q=0

    while q<12:
        for d in random.sample((e7),1):
            e8.append(d)
            e7.remove(d)
            q+=1

            break

    h8=e8[0][0]
    t8=e8[0][1]

    h9=e8[1][0]
    t9=e8[1][1]

    h10=e8[2][0]
    t10=e8[2][1]

    h11=e8[3][0]
    t11=e8[3][1]

    h12=e8[4][0]
    t12=e8[4][1]

    h13=e8[5][0]
    t13=e8[5][1]

    h14=e8[6][0]
    t14=e8[6][1]

    h15=e8[7][0]
    t15=e8[7][1]

    h16=e8[8][0]
    t16=e8[8][1]

    h17=e8[9][0]
    t17=e8[9][1]

    h18=e8[10][0]
    t18=e8[10][1]

    h19=e8[11][0]
    t19=e8[11][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",command=aşama9,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama7():
    global e6,e5,e4,e3,e2,e1,e

    h6=e6[0][0]
    t6=e6[0][1]
    
    e6.remove(e6[0])

    q=0

    while q<13:
        for d in random.sample((e6),1):
            e7.append(d)
            e6.remove(d)
            q+=1

            break

    h7=e7[0][0]
    t7=e7[0][1]

    h8=e7[1][0]
    t8=e7[1][1]

    h9=e7[2][0]
    t9=e7[2][1]

    h10=e7[3][0]
    t10=e7[3][1]

    h11=e7[4][0]
    t11=e7[4][1]

    h12=e7[5][0]
    t12=e7[5][1]

    h13=e7[6][0]
    t13=e7[6][1]

    h14=e7[7][0]
    t14=e7[7][1]

    h15=e7[8][0]
    t15=e7[8][1]

    h16=e7[9][0]
    t16=e7[9][1]

    h17=e7[10][0]
    t17=e7[10][1]

    h18=e7[11][0]
    t18=e7[11][1]

    h19=e7[12][0]
    t19=e7[12][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",command=aşama8,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama6():
    global e5,e4,e3,e2,e1,e

    h5=e5[0][0]
    t5=e5[0][1]
    
    e5.remove(e5[0])

    q=0

    while q<14:
        for d in random.sample((e5),1):
            e6.append(d)
            e5.remove(d)
            q+=1

            break

    h6=e6[0][0]
    t6=e6[0][1]

    h7=e6[1][0]
    t7=e6[1][1]

    h8=e6[2][0]
    t8=e6[2][1]

    h9=e6[3][0]
    t9=e6[3][1]

    h10=e6[4][0]
    t10=e6[4][1]

    h11=e6[5][0]
    t11=e6[5][1]

    h12=e6[6][0]
    t12=e6[6][1]

    h13=e6[7][0]
    t13=e6[7][1]

    h14=e6[8][0]
    t14=e6[8][1]

    h15=e6[9][0]
    t15=e6[9][1]

    h16=e6[10][0]
    t16=e6[10][1]

    h17=e6[11][0]
    t17=e6[11][1]

    h18=e6[12][0]
    t18=e6[12][1]

    h19=e6[13][0]
    t19=e6[13][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",command=aşama7,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama5():
    global e4,e3,e2,e1,e

    h4=e4[0][0]
    t4=e4[0][1]
    
    e4.remove(e4[0])

    q=0

    while q<15:
        for d in random.sample((e4),1):
            e5.append(d)
            e4.remove(d)
            q+=1

            break

    h5=e5[0][0]
    t5=e5[0][1]

    h6=e5[1][0]
    t6=e5[1][1]

    h7=e5[2][0]
    t7=e5[2][1]

    h8=e5[3][0]
    t8=e5[3][1]

    h9=e5[4][0]
    t9=e5[4][1]

    h10=e5[5][0]
    t10=e5[5][1]

    h11=e5[6][0]
    t11=e5[6][1]

    h12=e5[7][0]
    t12=e5[7][1]

    h13=e5[8][0]
    t13=e5[8][1]

    h14=e5[9][0]
    t14=e5[9][1]

    h15=e5[10][0]
    t15=e5[10][1]

    h16=e5[11][0]
    t16=e5[11][1]

    h17=e5[12][0]
    t17=e5[12][1]

    h18=e5[13][0]
    t18=e5[13][1]

    h19=e5[14][0]
    t19=e5[14][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",command=aşama6,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama4():
    global e3,e2,e1,e

    h3=e3[0][0]
    t3=e3[0][1]
    
    e3.remove(e3[0])

    q1=0

    while q1<16:
        for d in random.sample((e3),1):
            e4.append(d)
            e3.remove(d)
            q1+=1

            break

    h4=e4[0][0]
    t4=e4[0][1]

    h5=e4[1][0]
    t5=e4[1][1]

    h6=e4[2][0]
    t6=e4[2][1]

    h7=e4[3][0]
    t7=e4[3][1]

    h8=e4[4][0]
    t8=e4[4][1]

    h9=e4[5][0]
    t9=e4[5][1]

    h10=e4[6][0]
    t10=e4[6][1]

    h11=e4[7][0]
    t11=e4[7][1]

    h12=e4[8][0]
    t12=e4[8][1]

    h13=e4[9][0]
    t13=e4[9][1]

    h14=e4[10][0]
    t14=e4[10][1]

    h15=e4[11][0]
    t15=e4[11][1]

    h16=e4[12][0]
    t16=e4[12][1]

    h17=e4[13][0]
    t17=e4[13][1]

    h18=e4[14][0]
    t18=e4[14][1]

    h19=e4[15][0]
    t19=e4[15][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",command=aşama5,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)


def aşama3():
    global e2,e1,e

    h2=e2[0][0]
    t2=e2[0][1]

    e2.remove(e2[0])

    q1=0

    while q1<17:
        for d in random.sample((e2),1):
            e3.append(d)
            e2.remove(d)
            q1+=1

            break

    h3=e3[0][0]
    t3=e3[0][1]

    h4=e3[1][0]
    t4=e3[1][1]

    h5=e3[2][0]
    t5=e3[2][1]

    h6=e3[3][0]
    t6=e3[3][1]

    h7=e3[4][0]
    t7=e3[4][1]

    h8=e3[5][0]
    t8=e3[5][1]

    h9=e3[6][0]
    t9=e3[6][1]

    h10=e3[7][0]
    t10=e3[7][1]

    h11=e3[8][0]
    t11=e3[8][1]

    h12=e3[9][0]
    t12=e3[9][1]

    h13=e3[10][0]
    t13=e3[10][1]

    h14=e3[11][0]
    t14=e3[11][1]

    h15=e3[12][0]
    t15=e3[12][1]

    h16=e3[13][0]
    t16=e3[13][1]

    h17=e3[14][0]
    t17=e3[14][1]

    h18=e3[15][0]
    t18=e3[15][1]

    h19=e3[16][0]
    t19=e3[16][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #ikişer.place(relx = h1, rely = t1)
    
    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",command=aşama4,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

def aşama2():    
    global e1,e

    h1=e1[0][0]
    t1=e1[0][1]

    e1.remove(e1[0])

    q1=0

    while q1<18:
        for d in random.sample((e1),1):
            e2.append(d)
            e1.remove(d)
            q1+=1

            break

    h2=e2[0][0]
    t2=e2[0][1]

    h3=e2[1][0]
    t3=e2[1][1]

    h4=e2[2][0]
    t4=e2[2][1]

    h5=e2[3][0]
    t5=e2[3][1]

    h6=e2[4][0]
    t6=e2[4][1]

    h7=e2[5][0]
    t7=e2[5][1]

    h8=e2[6][0]
    t8=e2[6][1]

    h9=e2[7][0]
    t9=e2[7][1]

    h10=e2[8][0]
    t10=e2[8][1]

    h11=e2[9][0]
    t11=e2[9][1]

    h12=e2[10][0]
    t12=e2[10][1]

    h13=e2[11][0]
    t13=e2[11][1]

    h14=e2[12][0]
    t14=e2[12][1]

    h15=e2[13][0]
    t15=e2[13][1]

    h16=e2[14][0]
    t16=e2[14][1]

    h17=e2[15][0]
    t17=e2[15][1]

    h18=e2[16][0]
    t18=e2[16][1]

    h19=e2[17][0]
    t19=e2[17][1]

    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    #birer.place(relx = h , rely = t)
   
    ikişer = Button()
    ikişer.config(text="2",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",command=aşama3,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)
    
def aşama1():
    global e

    h=e[0][0]
    t=e[0][1]
   
    e.remove(e[0])

    q1=0

    while q1<19:
        for d in random.sample((e),1):
            e1.append(d)
            e.remove(d)
            q1+=1

            break

    h1=e1[0][0]
    t1=e1[0][1]

    h2=e1[1][0]
    t2=e1[1][1]

    h3=e1[2][0]
    t3=e1[2][1]

    h4=e1[3][0]
    t4=e1[3][1]

    h5=e1[4][0]
    t5=e1[4][1]

    h6=e1[5][0]
    t6=e1[5][1]

    h7=e1[6][0]
    t7=e1[6][1]

    h8=e1[7][0]
    t8=e1[7][1]

    h9=e1[8][0]
    t9=e1[8][1]

    h10=e1[9][0]
    t10=e1[9][1]

    h11=e1[10][0]
    t11=e1[10][1]

    h12=e1[11][0]
    t12=e1[11][1]

    h13=e1[12][0]
    t13=e1[12][1]

    h14=e1[13][0]
    t14=e1[13][1]

    h15=e1[14][0]
    t15=e1[14][1]

    h16=e1[15][0]
    t16=e1[15][1]

    h17=e1[16][0]
    t17=e1[16][1]

    h18=e1[17][0]
    t18=e1[17][1]

    h19=e1[18][0]
    t19=e1[18][1]
    
    birer = Button()
    birer.config(text="1",width=2,fg="yellow",bg="green",font="TTKBDikTemelAbece 20")
    birer.place(relx = h , rely = t)

    ikişer = Button()
    ikişer.config(text="2",command=aşama2,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer.place(relx = h1, rely = t1)

    birer1 = Button()
    birer1.config(text="3",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer1.place(relx = h2 , rely = t2)

    ikişer1 = Button()
    ikişer1.config(text="4",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer1.place(relx = h3, rely = t3)

    birer2 = Button()
    birer2.config(text="5",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer2.place(relx = h4 , rely = t4)

    ikişer2 = Button()
    ikişer2.config(text="6",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer2.place(relx = h5, rely = t5)

    birer3 = Button()
    birer3.config(text="7",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer3.place(relx = h6 , rely = t6)

    ikişer3 = Button()
    ikişer3.config(text="8",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer3.place(relx = h7, rely = t7)

    birer4 = Button()
    birer4.config(text="9",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer4.place(relx = h8 , rely = t8)

    ikişer4 = Button()
    ikişer4.config(text="10",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer4.place(relx = h9, rely = t9)

    birer5 = Button()
    birer5.config(text="11",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer5.place(relx = h10 , rely = t10)

    ikişer5 = Button()
    ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer5.place(relx = h11, rely = t11)

    birer6 = Button()
    birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer6.place(relx = h12 , rely = t12)

    ikişer6 = Button()
    ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer6.place(relx = h13, rely = t13)

    birer7 = Button()
    birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer7.place(relx = h14 , rely = t14)

    ikişer7 = Button()
    ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer7.place(relx = h15, rely = t15)

    birer8 = Button()
    birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer8.place(relx = h16 , rely = t16)

    ikişer8 = Button()
    ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer8.place(relx = h17, rely = t17)

    birer9 = Button()
    birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    birer9.place(relx = h18 , rely = t18)

    ikişer9 = Button()
    ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
    ikişer9.place(relx = h19, rely = t19)

qz=0

while qz<20:
    for d in random.sample((xy),1):
        e.append(d)
        xy.remove(d)
        qz+=1

        break

h=e[0][0]
t=e[0][1]

h1=e[1][0]
t1=e[1][1]

h2=e[2][0]
t2=e[2][1]

h3=e[3][0]
t3=e[3][1]

h4=e[4][0]
t4=e[4][1]

h5=e[5][0]
t5=e[5][1]

h6=e[6][0]
t6=e[6][1]

h7=e[7][0]
t7=e[7][1]

h8=e[8][0]
t8=e[8][1]

h9=e[9][0]
t9=e[9][1]

h10=e[10][0]
t10=e[10][1]

h11=e[11][0]
t11=e[11][1]

h12=e[12][0]
t12=e[12][1]

h13=e[13][0]
t13=e[13][1]

h14=e[14][0]
t14=e[14][1]

h15=e[15][0]
t15=e[15][1]

h16=e[16][0]
t16=e[16][1]

h17=e[17][0]
t17=e[17][1]

h18=e[18][0]
t18=e[18][1]

h19=e[19][0]
t19=e[19][1]

birer = Button()
birer.config(text="1",command=aşama1,width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer.place(relx = h , rely = t)

ikişer = Button()
ikişer.config(text="2",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer.place(relx = h1, rely = t1)

birer1 = Button()
birer1.config(text="3",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer1.place(relx = h2 , rely = t2)

ikişer1 = Button()
ikişer1.config(text="4",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer1.place(relx = h3, rely = t3)

birer2 = Button()
birer2.config(text="5",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer2.place(relx = h4 , rely = t4)

ikişer2 = Button()
ikişer2.config(text="6",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer2.place(relx = h5, rely = t5)

birer3 = Button()
birer3.config(text="7",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer3.place(relx = h6 , rely = t6)

ikişer3 = Button()
ikişer3.config(text="8",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer3.place(relx = h7, rely = t7)

birer4 = Button()
birer4.config(text="9",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer4.place(relx = h8 , rely = t8)

ikişer4 = Button()
ikişer4.config(text="10",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer4.place(relx = h9, rely = t9)

birer5 = Button()
birer5.config(text="11",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer5.place(relx = h10 , rely = t10)

ikişer5 = Button()
ikişer5.config(text="12",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer5.place(relx = h11, rely = t11)

birer6 = Button()
birer6.config(text="13",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer6.place(relx = h12 , rely = t12)

ikişer6 = Button()
ikişer6.config(text="14",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer6.place(relx = h13, rely = t13)

birer7 = Button()
birer7.config(text="15",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer7.place(relx = h14 , rely = t14)

ikişer7 = Button()
ikişer7.config(text="16",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer7.place(relx = h15, rely = t15)

birer8 = Button()
birer8.config(text="17",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer8.place(relx = h16 , rely = t16)

ikişer8 = Button()
ikişer8.config(text="18",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer8.place(relx = h17, rely = t17)

birer9 = Button()
birer9.config(text="19",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
birer9.place(relx = h18 , rely = t18)

ikişer9 = Button()
ikişer9.config(text="20",width=2,fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
ikişer9.place(relx = h19, rely = t19)

pygame.mixer.music.load("hello.ogg")
pygame.mixer.music.play(-1)

time11 = time.strftime("%H:%M:%S")
time1 = time.strftime("%H %M %S")

zaman1=time1.split()
saat1=int(zaman1[0])*3600
dakika1=int(zaman1[1])*60
saniye1=int(zaman1[2])
toplam1=saat1+dakika1+saniye1

sonu=Label(text="Oyuna Başlama Zamanı  "+time11,font="TTKBDikTemelAbece 16")
sonu.place(relx = 0.4, rely = 0.86)

buton=Button()
buton.config(text="ÇIKIŞ",command=pencere.destroy,width='10',fg="yellow",bg="red",font="TTKBDikTemelAbece 20")
buton.place(relx = 0.89, rely = 0.86)
      
pencere.mainloop()
