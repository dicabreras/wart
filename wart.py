import tkinter as tk
from tkinter import ttk 
from pruebas import *  # se importa el documpento tipo py llamado "pruebas"

def init_window(): # Funcion que abre la ventana principal de la aplicación 
  global window 
  global label_entrada1
  global label_entrada2
  global entrada1
  global entrada2
  global boton
  global incorrecto
  global cont
  
  window = tk.Tk() #crear la pantalla
  window.title('WART - Deutsch')
  window.geometry('500x400')
  window.configure(bg = 'gray14')
  
  label = tk.Label(window, text = 'WART-DEUTSCH', font = ('Arial Bold', 15), bg = 'firebrick3', fg = 'white')
  label.grid(column = 0, row = 0)

  entrada1 = tk.Entry(window, width = 15)
  entrada2 = tk.Entry(window, width = 15)

  entrada1.grid(column = 1, row = 1)
  entrada2.grid(column = 1, row = 2)

  label_entrada1 = tk.Label(window, text = 'Eingeben Sie ihren Nutzename:', font = ('Arial bold', 12), bg = 'gray5', fg = 'white')
  label_entrada1.grid(column = 0, row = 1)

  label_entrada2 = tk.Label(window, text = 'Eingeben Sie ihr Passwort', font = ('Arial bold', 12), bg='gray5', fg= 'white')
  label_entrada2.grid(column = 0, row = 2)
  
  incorrecto = False
  boton = tk.Button(window,                          
                 command = lambda: login(
                   entrada1.get(),
                   entrada2.get()), 
                 text = 'ALMENDUNG',
                 bg = 'black',
                 fg = 'yellow')
  boton.grid(column=1, row =6)      # boton principal de LOGIN
  cont = 0

  window.mainloop()
def borrar1():      #destruye las casillas de entrada correspondientes al usuario y contraseña del LOGIN     
  entrada1.destroy()
  entrada2.destroy()
  label_entrada1.destroy()
  label_entrada2.destroy()
  boton.destroy()  

def login(entrada1, entrada2): #función de LOGIN, donde esta configurado el usuario y la contraseña de acceso. También se configuro el "label" para mostrar el mensaje de que el usario fue correcto o incorrecto
  global label_correcto
  global incorrecto
  global label_incorrecto
  if entrada1 == 'admin' and entrada2 == '1234':
    if incorrecto == True:
      label_incorrecto.destroy()
      mostrar_categorias()
      label_correcto = tk.Label(window, text = '   Ihren Nutzename ist richtig   ', font =('Arial bold', 12), fg = 'white', bg = 'green')
      label_correcto.grid(column = 0, row = 10)
      borrar1()
    elif incorrecto == False:
       mostrar_categorias()
       label_correcto = tk.Label(window, text = '   Ihren Nutzename ist richtig   ', font =('Arial bold', 12), fg = 'white', bg = 'green')
       label_correcto.grid(column = 0, row = 10)
       borrar1()
  else:
    label_incorrecto = tk.Label(window, text = 'Ihren Nutzename ist schlecht', font = ('Arial bold', 12), fg = 'white', bg = 'red' )
    label_incorrecto.grid(column=0, row=10)
    incorrecto = True

def correcto_der(genero, cont):  #Para la opción del juego, se implementa unicamente si el articulo correcto del sustantivo a evaluar es "der"
  if genero == 'r':
    cont+=1
    label_score.configure(text = 'Gesamtpunktzahl: ' + str(cont))
    mostrar_comida(mas_palabras,cont, contador, cont1)
def correcto_das(genero, cont): #Para la opción del juego, se implementa unicamente si el articulo correcto del sustantivo a evaluar es "das"
  if genero =='s':
    cont+=1
    label_score.configure(text = 'Gesamtpunktzahl: ' + str(cont))
    mostrar_comida(mas_palabras, cont, contador, cont1)
def correcto_die(genero, cont): #Para la opción del juego, se implementa unicamente si el articulo correcto del sustantivo a evaluar es "die"
  if genero =='e':
    cont+=1
    label_score.configure(text = 'Gesamtpunktzahl: ' + str(cont))
    mostrar_comida(mas_palabras, cont, contador, cont1)

def masculino_der(): # Función que configura los botones de la opción "DER"
  global boton_der
  boton_der = tk.Button(window, 
         #         command = lambda: correcto_der(
          #        genero, cont),
                  text = '  DER  ',
                  bg = 'black',
                  fg = 'white',
                  font = ('Arial Bold', 12) )
  boton_der.grid(column=0, row = 4)                
def neutro_das():  # Función que configura los botones de la opción "DAS"
  global boton_das
  boton_das = tk.Button(window, 
   #               command = lambda: correcto_das(
    #              genero, cont),
                  text = '  DAS  ',
                  bg = 'yellow',
                  fg = 'black',
                  font = ('Arial Bold', 12) )
  boton_das.grid(column=1, row = 4)

def femenino_die(): # Función que configura los botones de la opción "DIE"
  global boton_die
  boton_die = tk.Button(window, 
    #              command = lambda: correcto_die(
     #             genero, cont),
                  text = '  DIE  ',
                  bg = 'red',
                  fg = 'white',
                  font = ('Arial Bold', 12) )
  boton_die.grid(column=3, row = 4)

def categorias(parte): # Función que destruye todos los widgets que estaban en la segunda ventana. Ademas pinta el contador de puntos y de acuerdo a la unidad que haya elegido el usuario, mostrara la sección de palabras correspondientes
  global label_score
  label_espacio.destroy()
  boton_jugar.destroy()
  boton_entrenar.destroy()
  combo_operadores.destroy()
  label_operador.destroy()
  label_general.destroy()
  boton1.destroy()
  masculino_der()
  label_espacio1 = tk.Label(window, text= '       ', bg = 'gray14') #posible retiro cuando se agreguen las imagenes
  label_espacio1.grid(column = 2, row = 4) 
  label_score = tk.Label(window, text = 'Gesamtpunktzahl: ', font = ('Arial bold', 12), bg = 'forest green', fg = 'black') 
  label_score.grid(column = 3, row = 0)
  neutro_das()
  femenino_die()
  ventana()
  if parte ==1:
    mostrar_comida(mas_palabras, cont, contador, cont1)
  elif parte == 2:
    mostrar_cuerpo()
  elif parte == 3:
    mostrar_animales()
  elif parte == 4:
    mostrar_cocina()
  elif parte == 5:
    mostrar_lugares()
  elif parte == 6:
    mostrar_casa()
  elif parte == 7:
    mostrar_medico()

def ventana(): #Función que invoca la ventana donde se empieza el juego o el entrenamiento
  global cont
  global contador
  global mas_palabras
  global cont1
  cont = 0
  cont1 = 1
  contador = str(cont1)
  label_espacio = tk.Label(window, text= '            ', bg = 'grey14')
  label_espacio.grid(column = 0, row = 1)
  mas_palabras = 0

def mostrar_comida(mas_palabras, cont, contador, cont1): #Función que muestra la lista de palabras cada vez que se seleccione el boton correcto correspondiente al genero que define al sustantivo

  while mas_palabras<= 6:
    global genero
    label_espacio1 = tk.Label(text='                                ', bg='grey14')
    if cont > 0:
      label_espacio1.grid(column = 0, row = 2)
      cont1+=1
      contador = str(cont1)
    palabra1 = lista_comida[cont]
    genero = palabra1[2]
    palabra = palabra1[3:]
    label_comida = tk.Label(window, text = palabra, font=('Arial bold', 13), bg = 'grey14', fg = 'white')
    label_comida.grid(column=0, row = 2)
    label_contador = tk.Label(window, text = 'Sustantiv: '+ contador, font =('Arial bold', 13), bg ='blue', fg='white')
    label_contador.grid(column= 0, row = 16)
    mas_palabras +=1

    if genero == 'e':
      boton_die.configure(command = lambda: correcto_die(genero, cont))
      mas_palabras+=1
      
    elif genero == 'r':
      boton_der.configure(command = lambda: correcto_der(genero, cont))
      mas_palabras+=1
    else:
      boton_das.configure(command = lambda: correcto_das(genero, cont))      
      mas_palabras+=1
   
   
 # label_genero = tk.Label(window, text = genero, font=('Arial bold', 13), bg = 'grey14', fg = 'red') #comprobando el genero de la palabra
 # label_genero.grid(column=0, row=3)  
  



def mostrar_cuerpo(): #Muestra los sustantivos correspondientes a entranar o evaluar en la categoria del cuerpo
  print('Der Körper')

def mostrar_animales(): #Muestra los sustantivos correspondientes a entranar o evaluar en la categoria de los animales
  print('Die Tiere')  

def mostrar_cocina(): #Muestra los sustantivos correspondientes a entranar o evaluar en la categoria de la cocina
  print('Die Küche')

def mostrar_lugares(): #Muestra los sustantivos correspondientes a entranar o evaluar en la categoria de los lugares
  print('Orte der Stadt')

def mostrar_casa(): #Muestra los sustantivos correspondientes a entranar o evaluar en la categoria de la casa
  print('Das Haus')

def mostrar_medico(): #Muestra los sustantivos correspondientes a entranar o evaluar en la categoria del médico
  print('Der Arztbesuch')

def mostrar_categorias():  #Funcion para mostrar las categorias que puede escoger el usuario para evaluarse o entrenarse
  global boton1
  global combo_operadores 
  global label_operador
  #crear una etiqueta para el seleccionador (combobox)
  label_operador = tk.Label(window, text = 'Wählen Sie einigen Kategorie', font = ('Arial bold', 12), bg = 'grey5', fg='white')
  label_operador.grid(column = 0, row = 4)
  #crear un seleccioador (combobox)
  combo_operadores = ttk.Combobox(window)
    #Aisgnar los valores del seleccionados a traves de un atributo values
  combo_operadores['values'] = [' ', '1. Das Lebensmittel', '2. Der Körper', '3. Die Tiere', '4. Die Küche', '5. Orte der Stadt', '6. Das Haus', '7. Der Arztbesuch']
    #Asignar por defecto una opcion seleccionada: 0 es el indice de los valores
  combo_operadores.current(0)#set te selected item
    #ubicar el seleccionador
  combo_operadores.grid(column=1, row=4)
  boton1 = tk.Button(window, command = lambda: escojer(
                        combo_operadores.get()),
                        text = 'WÄHLEN',
                        bg = 'DarkOrange3',
                        fg= 'white')
  boton1.grid(column=1, row = 5)     

                   
def escojer(combo): #Funcion que determina el valor de "parte", que corresponde a la categoria que escoja el usuario  
  global parte
  global label_general
  if combo == '1. Das Lebensmittel':
    label_correcto.destroy()
    label_general = tk.Label(window, text = '   Möchtest du...   ', font = ('Arial bold', 12), bg = 'red3', fg='white')
    label_general.grid(column = 0, row = 10)
    jugar()
    parte = 1
  elif combo == '2. Der Körper':
    label_correcto.destroy()
    label_general = tk.Label(window, text = '   Möchtest du...   ', font = ('Arial bold', 12), bg = 'red3', fg='white')
    label_general.grid(column = 0, row = 10)
    jugar()
    parte = 2
  elif combo == '3. Die Tiere':
    label_correcto.destroy()
    label_general = tk.Label(window, text = '   Möchtest du...   ', font = ('Arial bold', 12), bg = 'red3', fg='white')
    label_general.grid(column = 0, row = 10)
    jugar()
    parte = 3
  elif combo == '4. Die Küche':
    label_correcto.destroy()
    label_general = tk.Label(window, text = '   Möchtest du...   ', font = ('Arial bold', 12), bg = 'red3', fg='white')
    label_general.grid(column = 0, row = 10)
    jugar()
    parte =4
  elif combo == '5. Orte der Stadt':
    label_correcto.destroy()
    label_general = tk.Label(window, text = '   Möchtest du...   ', font = ('Arial bold', 12), bg = 'red3', fg='white')
    label_general.grid(column = 0, row = 10)
    jugar()
    parte = 5
  elif combo == '6. Das Haus':
    label_correcto.destroy()
    label_general = tk.Label(window, text = '   Möchtest du...   ', font = ('Arial bold', 12), bg = 'red3', fg='white')
    label_general.grid(column = 0, row = 10)   
    jugar()
    parte = 6  
  elif combo == '7. Der Arztbesuch':
    label_correcto.destroy()
    label_general = tk.Label(window, text = '   Möchtest du...   ', font = ('Arial bold', 12), bg = 'red3', fg='white')
    label_general.grid(column = 0, row = 5)
    jugar()
    parte = 7


def jugar():               # Función que construye los botones de "Jugar (spielen)" y "Entrenar (Trainieren)". Además los redirige a la función categorias
  global boton_jugar
  global label_espacio
  global boton_entrenar
  label_espacio = tk.Label(window, text= '            ', bg = 'gray14')
  label_espacio.grid(column = 0, row = 12)
  boton_jugar = tk.Button(window,
                     command = lambda: categorias(
                       parte),
                     text = 'SPIELEN',
                     bg = 'red3',
                     fg = 'white')
  boton_jugar.grid(column= 0, row = 14)  
  boton_entrenar = tk.Button(window,
                     command= lambda: categorias(
                          parte),
                          text = 'TRAINIEREN',
                          bg = 'DodgerBlue3',
                          fg = 'white')      
  boton_entrenar.grid(column= 1, row = 14)          

def main(): #Función principal. Que contiene la ventana del programa
  init_window()    

main()