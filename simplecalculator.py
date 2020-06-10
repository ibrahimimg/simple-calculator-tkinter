#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:55:23 2019

@author: ibrahim
"""

from tkinter import *
expression=" "
def press(num):
    global expression
    
    expression = expression+str(num)
    equation.set(expression)
    
def equal():
    global expression
    try:
        total=str(eval(expression))
        equation.set(total)
        expression=' '
    except:
        equation.set('Error')
        expression=' '
def clear():
    global expression
    equation.set(' ')
    expression=' '
def cl():
    global expression
    equation.set(expression[:-1])
    expression=expression[:-1]


    expf.grid(row=0,column=0,columnspan=4,ipadx=70)
if __name__ == "__main__":
    app=Tk()
    app.configure(background='green')
    app.title('Simple Calculator')
    app.geometry('307x200')
    
    equation=StringVar()
    expf=Entry(app,textvariable=equation)
    expf.grid(row=0,column=0,columnspan=4,ipadx=70)
    
    button1=Button(app,text='1',bg='blue',fg='black',width=7,height=1,command=lambda: press('1'))
    button1.grid(row=2,column=0)
    button2=Button(app,text='2',bg='blue',fg='black',width=7,height=1,command=lambda: press('2'))
    button2.grid(row=2,column=1)
    button=Button(app,text='3',bg='blue',fg='black',width=7,height=1,command=lambda: press('3'))
    button.grid(row=2,column=2)
    button=Button(app,text='/',bg='blue',fg='black',width=7,height=1,command=lambda: press('/'))
    button.grid(row=2,column=3)
    
    button=Button(app,text='4',bg='blue',fg='black',width=7,height=1,command=lambda: press('4'))
    button.grid(row=3,column=0)
    button=Button(app,text='5',bg='blue',fg='black',width=7,height=1,command=lambda: press('5'))
    button.grid(row=3,column=1)
    button=Button(app,text='6',bg='blue',fg='black',width=7,height=1,command=lambda: press('6'))
    button.grid(row=3,column=2)
    button=Button(app,text='*',bg='blue',fg='black',width=7,height=1,command=lambda: press('*'))
    button.grid(row=3,column=3)
    
    button=Button(app,text='7',bg='blue',fg='black',width=7,height=1,command=lambda: press('7'))
    button.grid(row=4,column=0)
    button=Button(app,text='8',bg='blue',fg='black',width=7,height=1,command=lambda: press('8'))
    button.grid(row=4,column=1)
    button=Button(app,text='9',bg='blue',fg='black',width=7,height=1,command=lambda: press('9'))
    button.grid(row=4,column=2)
    button=Button(app,text='-',bg='blue',fg='black',width=7,height=1,command=lambda: press('-'))
    button.grid(row=4,column=3)
    
    button=Button(app,text='0',bg='blue',fg='black',width=7,height=1,command=lambda: press('0'))
    button.grid(row=5,column=0)

    button=Button(app,text='<-',bg='blue',fg='black',width=7,height=1,command=cl)
    button.grid(row=5,column=1)
    button=Button(app,text='clear',bg='blue',fg='black',width=7,height=1,command=clear)
    button.grid(row=5,column=2)
    button=Button(app,text='+',bg='blue',fg='black',width=7,height=1,command=lambda: press('+'))
    button.grid(row=5,column=3)

    button=Button(app,text='=',bg='blue',fg='black',width=7,height=1,command=equal)
    button.grid(row=6,columnspan=4)
    app.mainloop()