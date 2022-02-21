from cmath import exp
from distutils import command
from sqlite3 import Row
from tkinter import *
from turtle import width
from unittest import result
import math

ventana = Tk() 
ventana.title("Calculadora")

i = 0

# Entrada 
e_texto = Entry(ventana, font=("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5)

# Funciones 

def clickBoton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
    
def borrar():
    e_texto.delete(0, END)
    i = 0

 
def hacerOperacion(i):
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0

#Función para borrar un solo caracter a la vez

def borrarUno():
    global i
    e_texto.delete(i)
    
    i -= 1
# Botones 

boton1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda: clickBoton(1))
boton2 = Button(ventana, text = "2", width = 5, height = 2, command = lambda: clickBoton(2))
boton3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda: clickBoton(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda: clickBoton(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda: clickBoton(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda: clickBoton(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda: clickBoton(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda: clickBoton(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda: clickBoton(9))
boton0 = Button(ventana, text = "0", width = 5, height = 2, command = lambda: clickBoton(0))

boton_borrar = Button(ventana, text = "AC", width = 5, height = 2, command = lambda: borrar())
boton_parentesis1 = Button(ventana, text = "(", width = 5, height = 2, command = lambda: clickBoton("("))
boton_parentesis2 = Button(ventana, text = ")", width = 5, height = 2, command = lambda: clickBoton(")"))
boton_punto = Button(ventana, text = ".", width = 5, height = 2, command = lambda: clickBoton("."))
boton_borrar1 = Button(ventana, text = "C", width = 5, height = 2, command = lambda: borrarUno())

boton_div = Button(ventana, text = "/", width = 5, height = 2, command = lambda: clickBoton("/"))
boton_mult = Button(ventana, text = "x", width = 5, height = 2, command = lambda: clickBoton("*"))
boton_sum = Button(ventana, text = "+", width = 5, height = 2, command = lambda: clickBoton("+"))
boton_rest = Button(ventana, text = "-", width = 5, height = 2, command = lambda: clickBoton("-"))
boton_igual = Button(ventana, text = "=", width = 5, height = 2, command = lambda: hacerOperacion("="))




# Agregar botones en pantalla 

boton_borrar.grid(row = 1, column =0, padx = 5, pady = 5)

boton_parentesis1.grid(row = 1, column =1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column =2, padx = 5, pady = 5)
boton_div.grid(row = 1, column =3, padx = 5, pady = 5)

#Botones de números
boton7.grid(row = 2, column =0, padx = 5, pady = 5)
boton8.grid(row = 2, column =1, padx = 5, pady = 5)
boton9.grid(row = 2, column =2, padx = 5, pady = 5)
boton_mult.grid(row = 2, column =3, padx = 5, pady = 5)

boton4.grid(row = 3, column =0, padx = 5, pady = 5)
boton5.grid(row = 3, column =1, padx = 5, pady = 5)
boton6.grid(row = 3, column =2, padx = 5, pady = 5)
boton_rest.grid(row = 3, column =3, padx = 5, pady = 5)

boton1.grid(row = 4, column =0, padx = 5, pady = 5)
boton2.grid(row = 4, column =1, padx = 5, pady = 5)
boton3.grid(row = 4, column =2, padx = 5, pady = 5)
boton_sum.grid(row = 4, column =3, padx = 5, pady = 5)
#
boton0.grid(row = 5, column =0, columnspan=1, padx = 5, pady = 5)
boton_borrar1.grid(row = 5, column =1, columnspan=1, padx = 5, pady = 5)
boton_punto.grid(row = 5, column =2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column =3, padx = 5, pady = 5)
#boton_sum.grid(row = 4, column =3, padx = 5, pady = 5)

# Botones de potenciación y radicación




ventana.mainloop()

