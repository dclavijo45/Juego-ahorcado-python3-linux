# Archivo: game.py
# Autor: Daniel Clavijo Gonzalez (danielclavijo19380@gmail.com)
# Fecha: 10/11/2020
# Descripción: Juego de ahorcado de toda la vida construido en python
#  y optimizado para linux, funciona apartir de una versión de python 3.X

import random, os

palabras = ['agua','paris','perro','juan','planeta']
intentoshechos = [] # registrar las letras digitadas
test1 = int(0) # verifica la primera instancia con el registro de palabras clave nueva
test2 = int(0) # verifica la entrada al menu 2 para no limpiar el log de el add palabra
test3 = int(0) # verifica la entrada al menu 1 para no limpiar el log de el add palabra
test4 = int(0) # verifica que el usuario no ponga numeros o una palabra invalida en el registro de palabra clave
test5 = int(0) # Verifica si se encontro la palabra clave para asi mostrarla en otro color
guia = int(0) # verifica si el usuario ingresó a modo guia (como se juega?)
detectaintentos = int(0) # detectar intentos fallidos
salir_de_partida = int(0) # verifica si ganó el juego
lista_intentos_unida_en_palabra = "" # los intentos los pasa a lista para ser validados
resultado = "" # es lo que se imprime "_" o la letra acertada
verresultado = "" # transformar el resultado quitandole los espacios
transformarverR = "" # se usa para la transformación de la palabra final luego de encontrada a mayúscula
lista_palabra_clave = [] # Transforma la palabra clave en lista para ser analizado el intento
# sistema acciones
def cleanS():
  os.system("clear")

# Acciones juego
def Palabra_Azar():
  global azar
  global asignacion
  azar = random.randint(0, len(palabras) - 1)
  asignacion = palabras[azar]

def Reg_palabras(palabra):
  global palabras
  global test1
  if test1 == 0:
    del palabras[:]
  if palabra in palabras:
    os.system("clear")
    os.system("echo "+"'" +"\e[34m"+"La palabra "+"\e[37m"+"\e[101m"+palabra+"\e[49m"+"\e[34m"+" está ya en la lista :)"+"\e[0m"+"'")
    print("")
  else:
    palabras = palabras + [palabra]
    os.system("clear")
    # 43 color ya existe en la lista
    os.system("echo "+"'" +"\e[36m"+"Se ha guardado "+"\e[35m"+palabra+"\e[36m" + " en la lista de palabras"+"\e[0m"+"'")
    print("")
  test1 = int(1)

# colores especiales antierror

def c_especial_azul(texto):
  c_azulef = "echo "+"'" +"\e[34m"+texto+"\e[30m"+"'"
  os.system(c_azulef)

def c_normal():
  c_normal = "echo " +" '"+ "\e[0m" + "'"
  os.system(c_normal)

# Colores
def c_rojoalerta(texto):
    c_rojoalert = "echo "+"'" +"\e[41m"+texto+"\e[0m"+"'"
    os.system(c_rojoalert)

def c_azul(texto):
  c_azulf = "echo "+"'" +"\e[34m"+texto+"\e[0m"+"'"
  os.system(c_azulf)

def c_cian(texto):
  c_cianf = "echo "+"'" +"\e[36m"+texto+"\e[0m"+"'"
  os.system(c_cianf)

def c_rojo(texto):
  c_rojof = "echo "+"'" +"\e[31m"+texto+"\e[0m"+"'"
  os.system(c_rojof)

def c_verde(texto):
  c_verdef = "echo "+"'" +"\e[32m"+texto+"\e[0m"+"'"
  os.system(c_verdef)

def c_naranja(texto):
  c_naranjaf = "echo "+"'" +"\e[33m"+texto+"\e[0m"+"'"
  os.system(c_naranjaf)

#INTENTOS MAN ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def int0():
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  c_rojo("+                                                                                  +")
  c_rojo("+                                      *---*                                       +")
  c_rojo("+                                      |   |                                       +")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                    #########                                     +")
  c_rojo("+                                                                                  +")
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("")

def int1():
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  c_rojo("+                                                                                  +")
  c_rojo("+                                      *---*                                       +")
  c_rojo("+                                      |   |                                       +")
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                      0"+"\e[31m"+"   |                                       +"+"'") #+"\e[30,"+"'"
  c_rojo("+                                          |                                       +")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                    #########                                     +")
  c_rojo("+                                                                                  +")
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("")

def int2():
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  c_rojo("+                                                                                  +")
  c_rojo("+                                      *---*                                       +")
  c_rojo("+                                      |   |                                       +")
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                      0"+"\e[31m"+"   |                                       +"+"'") #+"\e[30,"+"'"
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                      |  "+"\e[31m"+" |                                       +"+"'")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                    #########                                     +")
  c_rojo("+                                                                                  +")
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("")

def int3():
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  c_rojo("+                                                                                  +")
  c_rojo("+                                      *---*                                       +")
  c_rojo("+                                      |   |                                       +")
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                      0"+"\e[31m"+"   |                                       +"+"'") #+"\e[30,"+"'"
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                     /|  "+"\e[31m"+" |                                       +"+"'")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                    #########                                     +")
  c_rojo("+                                                                                  +")
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("")

def int4():
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  c_rojo("+                                                                                  +")
  c_rojo("+                                      *---*                                       +")
  c_rojo("+                                      |   |                                       +")
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                      0"+"\e[31m"+"   |                                       +"+"'") #+"\e[30,"+"'"
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                     /|\ "+"\e[31m"+" |                                       +"+"'")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                    #########                                     +")
  c_rojo("+                                                                                  +")
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("")

def int5():
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  c_rojo("+                                                                                  +")
  c_rojo("+                                      *---*                                       +")
  c_rojo("+                                      |   |                                       +")
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                      0"+"\e[31m"+"   |                                       +"+"'") #+"\e[30,"+"'"
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                     /|\ "+"\e[31m"+" |                                       +"+"'")
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                     /   "+"\e[31m"+" |                                       +"+"'")
  c_rojo("+                                          |                                       +")
  c_rojo("+                                    #########                                     +")
  c_rojo("+                                                                                  +")
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("")

def int6():
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  c_rojo("+                                                                                  +")
  c_rojo("+                                      *---*                                       +")
  c_rojo("+                                      |   |                                       +")
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                      0"+"\e[31m"+"   |                                       +"+"'") #+"\e[30,"+"'"
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                     /|\ "+"\e[31m"+" |                                       +"+"'")
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                     / \ "+"\e[31m"+" |                                       +"+"'")
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                        "+"\e[31m"+"  |                                       +"+"'")
  os.system("echo "+"'"+"\e[31m"+"+"+"\e[33m"+"                                    ^^^^^^^^^"+"\e[31m"+"                                     +"+"'")
  c_rojo("+                                                                                  +")
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  print("")
def MensajeBienvenido():
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
  c_rojo("+                                                                                  +")
  c_rojo("+                           Bienvenido al juego ahorcado!                          +")
  c_rojo("+                                                                                  +")
  c_rojo("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# verificar los intentos
def Intento0():
  global intentodigitado # letra digitada por el usuario
  global intentoshechos # lista de los intentos digitados por el usuario
  global lista_intentos_unida_en_palabra # la lista de intentos pasa a ser palabra unida
  global resultado # es lo que se imprime "_" o la letra acertada 
  global verresultado # es para cuando la palabra llegue a ser descubierta, entonces le quite los " " y
  #                      la compare con la palabra clave 
  global pasado_a_minusculas # se transforma la letra digitada a minusculas luego de su verificación
  global lista_palabra_clave
  global detectaintentos # descripcion ARRIBA
  global salir_de_partida # descripcion ARRIBA
  verresultado = resultado.replace(" ", "")
  if verresultado == asignacion: # se compara si la palabra clave ya fue descubierta para proceder a mostrar el
    #                              mensaje final de ganador
    del resultado # se borra la variable para iniciar nuevo juego
    resultado = "" # se crea la variable vacia para iniciar nuevo juego
    del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
    lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
    formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
    del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
    intentoshechos = formatearintentoslista # reasignacion de lista vacia
    detectaintentos = int(-1) # se resetea los intentos fallidos
    print("")
    c_naranja("                              Haz encontrado la palabra!")
    del detectaintentos # se eliminan los intentos para poder jugar de nuevo
    detectaintentos = int(0) # se crea la variable para volver a jugar
    salir_de_partida = int(1)
    print("")
    c_cian("                            Presiona Enter para continuar...")
    input()
    cleanS()
  else:
    print("")
    c_azul("Digita una letra y presiona Enter: ")
    print("")
    while(True): # verificacion de si es letra o no, y si es 1 solo caracter 
      intentodigitado = input()
      if intentodigitado not in 'abcdefghijklmnopqrstuvwxyz':
        cleanS() # limpieza de pantalla
        int0() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
        ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
        print("")
        c_rojoalerta("Digita una letra válida y presiona Enter!")
        print("")
      else:
        if len(intentodigitado) != 1:
          cleanS() # limpieza de pantalla
          int0() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
          ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
          print("")
          c_rojoalerta("Digita una letra válida y presiona Enter!")
          print("")
        else: # se valida la letra digitada como correcta
          pasado_a_minusculas = intentodigitado.lower()
          
          # LLAVE DE ORO
          lista_palabra_clave = list(asignacion)

          if pasado_a_minusculas in intentoshechos: # verificacion si la nueva letra digitada no está en la
            #                                         lista antes de agregarla
            cleanS()
            int0()
            ImprimirEstado()
            print("")
            os.system("echo "+"'"+"\e[32m"+"                                 Ya usaste esta letra! "+"\e[0m"+"'")
            print("")
            c_cian("                            Presiona Enter para continuar...")
            input()
            break
          else:
            intentoshechos = intentoshechos + [pasado_a_minusculas] # se agrega la letra a la lista de los intentos
            lista_intentos_unida_en_palabra = "".join(intentoshechos) # se transforma de la lista a palabra
            
            if pasado_a_minusculas in lista_palabra_clave: # validación para ver si el intento fue fallido o no
              pass
            else:
              detectaintentos = detectaintentos + 1 # se suman los intentos fallidos para asi mostrar otro man
            break

def Intento1():
  global intentodigitado # letra digitada por el usuario
  global intentoshechos # lista de los intentos digitados por el usuario
  global lista_intentos_unida_en_palabra # la lista de intentos pasa a ser palabra unida
  global resultado # es lo que se imprime "_" o la letra acertada 
  global verresultado # es para cuando la palabra llegue a ser descubierta, entonces le quite los " " y
  #                      la compare con la palabra clave 
  global pasado_a_minusculas # se transforma la letra digitada a minusculas luego de su verificación
  global lista_palabra_clave
  global detectaintentos # descripcion ARRIBA
  global salir_de_partida # descripcion ARRIBA
  verresultado = resultado.replace(" ", "")
  if verresultado == asignacion: # se compara si la palabra clave ya fue descubierta para proceder a mostrar el
    #                              mensaje final de ganador
    del resultado # se borra la variable para iniciar nuevo juego
    resultado = "" # se crea la variable vacia para iniciar nuevo juego
    del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
    lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
    formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
    del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
    intentoshechos = formatearintentoslista # reasignacion de lista vacia
    detectaintentos = int(-1) # se resetea los intentos fallidos
    print("")
    c_naranja("                              Haz encontrado la palabra!")
    salir_de_partida = int(1)
    del detectaintentos # se eliminan los intentos para poder jugar de nuevo
    detectaintentos = int(0) # se crea la variable para volver a jugar
    print("")
    c_cian("                            Presiona Enter para continuar...")
    input()
    cleanS()
  else:
    print("")
    c_azul("Digita una letra y presiona Enter: ")
    print("")
    while(True): # verificacion de si es letra o no, y si es 1 solo caracter 
      intentodigitado = input()
      if intentodigitado not in 'abcdefghijklmnopqrstuvwxyz':
        cleanS() # limpieza de pantalla
        int1() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
        ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
        print("")
        c_rojoalerta("Digita una letra válida y presiona Enter!")
        print("")
      else:
        if len(intentodigitado) != 1:
          cleanS() # limpieza de pantalla
          int1() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
          ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
          print("")
          c_rojoalerta("Digita una letra válida y presiona Enter!")
          print("")
        else: # se valida la letra digitada como correcta
          pasado_a_minusculas = intentodigitado.lower()
          
          # LLAVE DE ORO
          lista_palabra_clave = list(asignacion)
          if pasado_a_minusculas in intentoshechos: # verificacion si la nueva letra digitada no está en la
            #                                         lista antes de agregarla
            cleanS()
            int1()
            ImprimirEstado()
            print("")
            os.system("echo "+"'"+"\e[32m"+"                                 Ya usaste esta letra! "+"\e[0m"+"'")
            print("")
            c_cian("                            Presiona Enter para continuar...")
            input()
            break
          else:
            intentoshechos = intentoshechos + [pasado_a_minusculas] # se agrega la letra a la lista de los intentos
            lista_intentos_unida_en_palabra = "".join(intentoshechos) # se transforma de la lista a palabra
            
            if pasado_a_minusculas in lista_palabra_clave: # validación para ver si el intento fue fallido o no
              pass
            else:
              detectaintentos = detectaintentos + 1 # se suman los intentos fallidos para asi mostrar otro man
            break

def Intento2():
  global intentodigitado # letra digitada por el usuario
  global intentoshechos # lista de los intentos digitados por el usuario
  global lista_intentos_unida_en_palabra # la lista de intentos pasa a ser palabra unida
  global resultado # es lo que se imprime "_" o la letra acertada 
  global verresultado # es para cuando la palabra llegue a ser descubierta, entonces le quite los " " y
  #                      la compare con la palabra clave 
  global pasado_a_minusculas # se transforma la letra digitada a minusculas luego de su verificación
  global lista_palabra_clave
  global detectaintentos # descripcion ARRIBA
  global salir_de_partida # descripcion ARRIBA
  verresultado = resultado.replace(" ", "")
  if verresultado == asignacion: # se compara si la palabra clave ya fue descubierta para proceder a mostrar el
    #                              mensaje final de ganador
    del resultado # se borra la variable para iniciar nuevo juego
    resultado = "" # se crea la variable vacia para iniciar nuevo juego
    del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
    lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
    formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
    del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
    intentoshechos = formatearintentoslista # reasignacion de lista vacia
    detectaintentos = int(-1) # se resetea los intentos fallidos
    print("")
    c_naranja("                              Haz encontrado la palabra!")
    salir_de_partida = int(1)
    del detectaintentos # se eliminan los intentos para poder jugar de nuevo
    detectaintentos = int(0) # se crea la variable para volver a jugar
    print("")
    c_cian("                            Presiona Enter para continuar...")
    input()
    cleanS()
  else:
    print("")
    c_azul("Digita una letra y presiona Enter: ")
    print("")
    while(True): # verificacion de si es letra o no, y si es 1 solo caracter 
      intentodigitado = input()
      if intentodigitado not in 'abcdefghijklmnopqrstuvwxyz':
        cleanS() # limpieza de pantalla
        int2() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
        ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
        print("")
        c_rojoalerta("Digita una letra y presiona válida y presiona Enter!")
        print("")
      else:
        if len(intentodigitado) != 1:
          cleanS() # limpieza de pantalla
          int2() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
          ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
          print("")
          c_rojoalerta("Digita una letra válida y presiona Enter!")
          print("")
        else: # se valida la letra digitada como correcta
          pasado_a_minusculas = intentodigitado.lower()
          
          # LLAVE DE ORO
          lista_palabra_clave = list(asignacion)
          if pasado_a_minusculas in intentoshechos: # verificacion si la nueva letra digitada no está en la
            #                                         lista antes de agregarla
            cleanS()
            int2()
            ImprimirEstado()
            print("")
            os.system("echo "+"'"+"\e[32m"+"                                 Ya usaste esta letra! "+"\e[0m"+"'")
            print("")
            c_cian("                            Presiona Enter para continuar...")
            input()
            break
          else:
            intentoshechos = intentoshechos + [pasado_a_minusculas] # se agrega la letra a la lista de los intentos
            lista_intentos_unida_en_palabra = "".join(intentoshechos) # se transforma de la lista a palabra
            
            if pasado_a_minusculas in lista_palabra_clave: # validación para ver si el intento fue fallido o no
              pass
            else:
              detectaintentos = detectaintentos + 1 # se suman los intentos fallidos para asi mostrar otro man
            break

def Intento3():
  global intentodigitado # letra digitada por el usuario
  global intentoshechos # lista de los intentos digitados por el usuario
  global lista_intentos_unida_en_palabra # la lista de intentos pasa a ser palabra unida
  global resultado # es lo que se imprime "_" o la letra acertada 
  global verresultado # es para cuando la palabra llegue a ser descubierta, entonces le quite los " " y
  #                      la compare con la palabra clave 
  global pasado_a_minusculas # se transforma la letra digitada a minusculas luego de su verificación
  global lista_palabra_clave
  global detectaintentos # descripcion ARRIBA
  global salir_de_partida # descripcion ARRIBA
  verresultado = resultado.replace(" ", "")
  if verresultado == asignacion: # se compara si la palabra clave ya fue descubierta para proceder a mostrar el
    #                              mensaje final de ganador
    del resultado # se borra la variable para iniciar nuevo juego
    resultado = "" # se crea la variable vacia para iniciar nuevo juego
    del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
    lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
    formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
    del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
    intentoshechos = formatearintentoslista # reasignacion de lista vacia
    detectaintentos = int(-1) # se resetea los intentos fallidos
    print("")
    c_naranja("                              Haz encontrado la palabra!")
    salir_de_partida = int(1)
    del detectaintentos # se eliminan los intentos para poder jugar de nuevo
    detectaintentos = int(0) # se crea la variable para volver a jugar
    print("")
    c_cian("                            Presiona Enter para continuar...")
    input()
    cleanS()
  else:
    print("")
    c_azul("Digita una letra y presiona Enter: ")
    print("")
    while(True): # verificacion de si es letra o no, y si es 1 solo caracter 
      intentodigitado = input()
      if intentodigitado not in 'abcdefghijklmnopqrstuvwxyz':
        cleanS() # limpieza de pantalla
        int3() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
        ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
        print("")
        c_rojoalerta("Digita una letra válida y presiona Enter!")
        print("")
      else:
        if len(intentodigitado) != 1:
          cleanS() # limpieza de pantalla
          int3() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
          ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
          print("")
          c_rojoalerta("Digita una letra válida y presiona Enter!")
          print("")
        else: # se valida la letra digitada como correcta
          pasado_a_minusculas = intentodigitado.lower()
          
          # LLAVE DE ORO
          lista_palabra_clave = list(asignacion)
          if pasado_a_minusculas in intentoshechos: # verificacion si la nueva letra digitada no está en la
            #                                         lista antes de agregarla
            cleanS()
            int3()
            ImprimirEstado()
            print("")
            os.system("echo "+"'"+"\e[32m"+"                                 Ya usaste esta letra! "+"\e[0m"+"'")
            print("")
            c_cian("                            Presiona Enter para continuar...")
            input()
            break
          else:
            intentoshechos = intentoshechos + [pasado_a_minusculas] # se agrega la letra a la lista de los intentos
            lista_intentos_unida_en_palabra = "".join(intentoshechos) # se transforma de la lista a palabra
            
            if pasado_a_minusculas in lista_palabra_clave: # validación para ver si el intento fue fallido o no
              pass
            else:
              detectaintentos = detectaintentos + 1 # se suman los intentos fallidos para asi mostrar otro man
            break

def Intento4():
  global intentodigitado # letra digitada por el usuario
  global intentoshechos # lista de los intentos digitados por el usuario
  global lista_intentos_unida_en_palabra # la lista de intentos pasa a ser palabra unida
  global resultado # es lo que se imprime "_" o la letra acertada 
  global verresultado # es para cuando la palabra llegue a ser descubierta, entonces le quite los " " y
  #                      la compare con la palabra clave 
  global pasado_a_minusculas # se transforma la letra digitada a minusculas luego de su verificación
  global lista_palabra_clave
  global detectaintentos # descripcion ARRIBA
  global salir_de_partida # descripcion ARRIBA
  verresultado = resultado.replace(" ", "")
  if verresultado == asignacion: # se compara si la palabra clave ya fue descubierta para proceder a mostrar el
    #                              mensaje final de ganador
    del resultado # se borra la variable para iniciar nuevo juego
    resultado = "" # se crea la variable vacia para iniciar nuevo juego
    del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
    lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
    formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
    del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
    intentoshechos = formatearintentoslista # reasignacion de lista vacia
    detectaintentos = int(-1) # se resetea los intentos fallidos
    print("")
    c_naranja("                              Haz encontrado la palabra!")
    salir_de_partida = int(1)
    del detectaintentos # se eliminan los intentos para poder jugar de nuevo
    detectaintentos = int(0) # se crea la variable para volver a jugar
    print("")
    c_cian("                            Presiona Enter para continuar...")
    input()
    cleanS()
  else:
    print("")
    c_azul("Digita una letra y presiona Enter: ")
    print("")
    while(True): # verificacion de si es letra o no, y si es 1 solo caracter 
      intentodigitado = input()
      if intentodigitado not in 'abcdefghijklmnopqrstuvwxyz':
        cleanS() # limpieza de pantalla
        int4() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
        ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
        print("")
        c_rojoalerta("Digita una letra válida y presiona Enter!")
        print("")
      else:
        if len(intentodigitado) != 1:
          cleanS() # limpieza de pantalla
          int4() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
          ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
          print("")
          c_rojoalerta("Digita una letra válida y presiona Enter!")
          print("")
        else: # se valida la letra digitada como correcta
          pasado_a_minusculas = intentodigitado.lower()
          
          # LLAVE DE ORO
          lista_palabra_clave = list(asignacion)
          if pasado_a_minusculas in intentoshechos: # verificacion si la nueva letra digitada no está en la
            #                                         lista antes de agregarla
            cleanS()
            int4()
            ImprimirEstado()
            print("")
            os.system("echo "+"'"+"\e[32m"+"                                 Ya usaste esta letra! "+"\e[0m"+"'")
            print("")
            c_cian("                            Presiona Enter para continuar...")
            input()
            break
          else:
            intentoshechos = intentoshechos + [pasado_a_minusculas] # se agrega la letra a la lista de los intentos
            lista_intentos_unida_en_palabra = "".join(intentoshechos) # se transforma de la lista a palabra
            
            if pasado_a_minusculas in lista_palabra_clave: # validación para ver si el intento fue fallido o no
              pass
            else:
              detectaintentos = detectaintentos + 1 # se suman los intentos fallidos para asi mostrar otro man
            break

def Intento5():
  global intentodigitado # letra digitada por el usuario
  global intentoshechos # lista de los intentos digitados por el usuario
  global lista_intentos_unida_en_palabra # la lista de intentos pasa a ser palabra unida
  global resultado # es lo que se imprime "_" o la letra acertada 
  global verresultado # es para cuando la palabra llegue a ser descubierta, entonces le quite los " " y
  #                      la compare con la palabra clave 
  global pasado_a_minusculas # se transforma la letra digitada a minusculas luego de su verificación
  global lista_palabra_clave
  global detectaintentos # descripcion ARRIBA
  global salir_de_partida # descripcion ARRIBA
  verresultado = resultado.replace(" ", "")
  if verresultado == asignacion: # se compara si la palabra clave ya fue descubierta para proceder a mostrar el
    #                              mensaje final de ganador
    del resultado # se borra la variable para iniciar nuevo juego
    resultado = "" # se crea la variable vacia para iniciar nuevo juego
    del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
    lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
    formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
    del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
    intentoshechos = formatearintentoslista # reasignacion de lista vacia
    detectaintentos = int(-1) # se resetea los intentos fallidos
    print("")
    c_naranja("                              Haz encontrado la palabra!")
    salir_de_partida = int(1)
    del detectaintentos # se eliminan los intentos para poder jugar de nuevo
    detectaintentos = int(0) # se crea la variable para volver a jugar
    print("")
    c_cian("                            Presiona Enter para continuar...")
    input()
    cleanS()
  else:
    print("")
    c_azul("Digita una letra y presiona Enter: ")
    print("")
    while(True): # verificacion de si es letra o no, y si es 1 solo caracter 
      intentodigitado = input()
      if intentodigitado not in 'abcdefghijklmnopqrstuvwxyz':
        cleanS() # limpieza de pantalla
        int5() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
        ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
        print("")
        c_rojoalerta("Digita una letra válida y presiona Enter!")
        print("")
      else:
        if len(intentodigitado) != 1:
          cleanS() # limpieza de pantalla
          int5() # mostrar el mansito con estado de ahorcado con respecto a los intentos fallidos
          ImprimirEstado() # se procede a mostrar el estado de los intentos de la palabra clave
          print("")
          c_rojoalerta("Digita una letra válida y presiona Enter!")
          print("")
        else: # se valida la letra digitada como correcta
          pasado_a_minusculas = intentodigitado.lower()
          
          # LLAVE DE ORO
          lista_palabra_clave = list(asignacion)
          if pasado_a_minusculas in intentoshechos: # verificacion si la nueva letra digitada no está en la
            #                                         lista antes de agregarla
            cleanS()
            int5()
            ImprimirEstado()
            print("")
            os.system("echo "+"'"+"\e[32m"+"                                 Ya usaste esta letra! "+"\e[0m"+"'")
            print("")
            c_cian("                            Presiona Enter para continuar...")
            input()
            break
          else:
            intentoshechos = intentoshechos + [pasado_a_minusculas] # se agrega la letra a la lista de los intentos
            lista_intentos_unida_en_palabra = "".join(intentoshechos) # se transforma de la lista a palabra
            
            if pasado_a_minusculas in lista_palabra_clave: # validación para ver si el intento fue fallido o no
              pass
            else:
              detectaintentos = detectaintentos + 1 # se suman los intentos fallidos para asi mostrar otro man
            break

# Analizar la letra y colocar _ ó la letra si esta en la palabra +++++++++++++
def ImprimirEstado():
  global asignacion # palabra clave
  global resultado # es lo que se imprime "_" o la letra acertada
  global lista_intentos_unida_en_palabra # la lista de intentos pasa a ser palabra unida
  global test5 # descripcion ARRIBA
  global verresultado # se asignara para hacer la validación de si se completó para asi asignarle color
  global transformarverR # se usa para la transformación de la palabra final luego de encontrada a mayúscula
  resultado = "" # Elimina  los "_ " y letras añadidas en la primer vuelta
  # algoritmo maestro, asigna a resultado "_ " o la letra + " " - acertada
  for palabra in asignacion:
    for letra in palabra:
      if letra in lista_intentos_unida_en_palabra:
        resultado += letra + " "
      else:
        resultado += "_ "

  verresultado = resultado.replace(" ", "") # se usa para revisar si finalizó y asi asignar color

  if verresultado == asignacion: # validación de asignacion de color al finalizar
    test5 = int(1)
    transformarverR = resultado.upper() # asignación de palabra final con color en mayúsculas

  if test5 == 1: # validación de cambio de color al finalizar
    os.system("echo "+"'" +"\e[35m"+"                                     "+transformarverR+"\e[0m"+"'")
    del transformarverR # se borra para ser reasignado
    transformarverR = "" # reseteo para nuevo uso
    test5 = int(0) # reseteo de testigo para no asignar color a la palabra clave nuevamente

  else:
    print("                                    ",resultado) # imprime "_" o la letra acertada

  #Deteccion_acertacion() ejecucion de mostrar si acertó la letra o no

def Deteccion_acertacion():
   detectaintentos = detectaintentos + 1 # por cada vez que digite una letra incorrecta, se sumara
  #                                       para mostrar el man ahorcado diferente

# Menu 1
while(True):
  if test3 == 0: # validacion si entra normal, si es 1 borra la pantalla debido a que no se uso la opción comenzar
    cleanS()
  test3 = int(0) # testigo reseteado
  MensajeBienvenido()
  print("")
  c_verde("                                Elije y presiona Enter:")
  print("")
  c_azul("                                1- Comenzar!  2- Salír  ")
  print("")
  op = input()
  # ingreso menu 1, comenzar
  if op == "1":
    while(True): # caja de menu 2
      if test2 == 0: # validacion si entra normal, si es 1 borra la pantalla debido a que no se uso la opción jugar
        cleanS()
      salir_de_partida = int(0) # se resetea para volver a jugar
      test2 = int(1) # testigo reseteado
      MensajeBienvenido()
      print("")
      c_verde("                                Elije y presiona Enter:")
      print("")
      c_azul("        -1 Jugar  -2 Poner palabras clave  -3 Listar palabras clave  -4 Salir")
      print("")
      op = input()
      # ingreso menu 2, jugar
      if op == "1":
        Palabra_Azar() # se crea la palabra clave 
        while(True): # caja de jugar
          # intento #1
          if detectaintentos == 0:   # se valida en que intento va, solo se permite máximo 6 intentos
            cleanS() # limpieza de pantalla
            verresultado = resultado.replace(" ", "") # borrar espacios de verresultado para ser analizado
            # verificacion de si veresultado (palabra en la salida de "_" o letra) es igual a la palabra clave
            # para asi determinar que ganó el juego
            if verresultado == asignacion:
              del resultado # se borra la variable para iniciar nuevo juego
              resultado = "" # se crea la variable vacia para iniciar nuevo juego
              del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
              lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
              formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
              del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
              intentoshechos = formatearintentoslista # reasignacion de lista vacia
              del detectaintentos  # se borra los intentos fallidos
              detectaintentos = int(0) # se vuelve a crear la variable para ejecutar los intentos
              print("")
              c_naranja("                              Haz encontrado la palabra!")
              salir_de_partida = int(1) # descripcion ARRIBA
              print("")
              del detectaintentos # se eliminan los intentos para poder jugar de nuevo
              detectaintentos = int(0) # se crea la variable para volver a jugar
              c_cian("                            Presiona Enter para continuar...")
              input()
              cleanS()
              break # se sale de la #caja jugar
            else:
              int0() # muestra el man ahorcado segun el intento actual
              ImprimirEstado() # coloca "_ " o la letra de acuerdo a la palabra clave
              Intento0() # se hace previa validación de la letra, se agrega la letra digitada a la lista de
              #            los intentos, se une la lista de los intentos en una palabra para poder se usada
              #            para recorrerse y asi mostrar alguna letra que esté en la palabra clave
              if salir_de_partida == 1: # al detectar que adivinó la palabra, se procede a salir
                break
          elif detectaintentos == 1:
            cleanS() # limpieza de pantalla
            verresultado = resultado.replace(" ", "") # borrar espacios de verresultado para ser analizado
            # verificacion de si veresultado (palabra en la salida de "_" o letra) es igual a la palabra clave
            # para asi determinar que ganó el juego
            if verresultado == asignacion:
              del resultado # se borra la variable para iniciar nuevo juego
              resultado = "" # se crea la variable vacia para iniciar nuevo juego
              del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
              lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
              formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
              del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
              intentoshechos = formatearintentoslista # reasignacion de lista vacia
              detectaintentos = int(-1) # se resetea los intentos fallidos
              print("")
              c_naranja("                              Haz encontrado la palabra!")
              salir_de_partida = int(1) # descripcion ARRIBA
              del detectaintentos # se eliminan los intentos para poder jugar de nuevo
              detectaintentos = int(0) # se crea la variable para volver a jugar
              print("")
              c_cian("                            Presiona Enter para continuar...")
              input()
              cleanS()
              break # se sale de la #caja jugar
            else:
              int1() # muestra el man ahorcado segun el intento actual
              ImprimirEstado() # coloca "_ " o la letra de acuerdo a la palabra clave
              Intento1() # se hace previa validación de la letra, se agrega la letra digitada a la lista de
              #            los intentos, se une la lista de los intentos en una palabra para poder se usada
              #            para recorrerse y asi mostrar alguna letra que esté en la palabra clave
              if salir_de_partida == 1: # al detectar que adivinó la palabra, se procede a salir
                break
          elif detectaintentos == 2:
            cleanS() # limpieza de pantalla
            verresultado = resultado.replace(" ", "") # borrar espacios de verresultado para ser analizado
            # verificacion de si veresultado (palabra en la salida de "_" o letra) es igual a la palabra clave
            # para asi determinar que ganó el juego
            if verresultado == asignacion:
              del resultado # se borra la variable para iniciar nuevo juego
              resultado = "" # se crea la variable vacia para iniciar nuevo juego
              del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
              lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
              formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
              del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
              intentoshechos = formatearintentoslista # reasignacion de lista vacia
              detectaintentos = int(-1) # se resetea los intentos fallidos
              print("")
              c_naranja("                              Haz encontrado la palabra!")
              salir_de_partida = int(1) # descripcion ARRIBA
              del detectaintentos # se eliminan los intentos para poder jugar de nuevo
              detectaintentos = int(0) # se crea la variable para volver a jugar
              print("")
              c_cian("                            Presiona Enter para continuar...")
              input()
              cleanS()
              break # se sale de la #caja jugar
            else:
              int2() # muestra el man ahorcado segun el intento actual
              ImprimirEstado() # coloca "_ " o la letra de acuerdo a la palabra clave
              Intento2() # se hace previa validación de la letra, se agrega la letra digitada a la lista de
              #            los intentos, se une la lista de los intentos en una palabra para poder se usada
              #            para recorrerse y asi mostrar alguna letra que esté en la palabra clave
              if salir_de_partida == 1: # al detectar que adivinó la palabra, se procede a salir
                break
          elif detectaintentos == 3:
            cleanS() # limpieza de pantalla
            verresultado = resultado.replace(" ", "") # borrar espacios de verresultado para ser analizado
            # verificacion de si veresultado (palabra en la salida de "_" o letra) es igual a la palabra clave
            # para asi determinar que ganó el juego
            if verresultado == asignacion:
              del resultado # se borra la variable para iniciar nuevo juego
              resultado = "" # se crea la variable vacia para iniciar nuevo juego
              del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
              lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
              formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
              del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
              intentoshechos = formatearintentoslista # reasignacion de lista vacia
              detectaintentos = int(-1) # se resetea los intentos fallidos
              print("")
              c_naranja("                              Haz encontrado la palabra!")
              salir_de_partida = int(1) # descripcion ARRIBA
              del detectaintentos # se eliminan los intentos para poder jugar de nuevo
              detectaintentos = int(0) # se crea la variable para volver a jugar
              print("")
              c_cian("                            Presiona Enter para continuar...")
              input()
              cleanS()
              break # se sale de la #caja jugar
            else:
              int3() # muestra el man ahorcado segun el intento actual
              ImprimirEstado() # coloca "_ " o la letra de acuerdo a la palabra clave
              Intento3() # se hace previa validación de la letra, se agrega la letra digitada a la lista de
              #            los intentos, se une la lista de los intentos en una palabra para poder se usada
              #            para recorrerse y asi mostrar alguna letra que esté en la palabra clave
              if salir_de_partida == 1: # al detectar que adivinó la palabra, se procede a salir
                break
          elif detectaintentos == 4:
            cleanS() # limpieza de pantalla
            verresultado = resultado.replace(" ", "") # borrar espacios de verresultado para ser analizado
            # verificacion de si veresultado (palabra en la salida de "_" o letra) es igual a la palabra clave
            # para asi determinar que ganó el juego
            if verresultado == asignacion:
              del resultado # se borra la variable para iniciar nuevo juego
              resultado = "" # se crea la variable vacia para iniciar nuevo juego
              del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
              lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
              formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
              del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
              intentoshechos = formatearintentoslista # reasignacion de lista vacia
              print("")
              c_naranja("                              Haz encontrado la palabra!")
              salir_de_partida = int(1) # descripcion ARRIBA
              del detectaintentos # se eliminan los intentos para poder jugar de nuevo
              detectaintentos = int(0) # se crea la variable para volver a jugar
              print("")
              c_cian("                            Presiona Enter para continuar...")
              input()
              cleanS()
              break # se sale de la #caja jugar
            else:
              int4() # muestra el man ahorcado segun el intento actual
              ImprimirEstado() # coloca "_ " o la letra de acuerdo a la palabra clave
              Intento4() # se hace previa validación de la letra, se agrega la letra digitada a la lista de
              #            los intentos, se une la lista de los intentos en una palabra para poder se usada
              #            para recorrerse y asi mostrar alguna letra que esté en la palabra clave
              if salir_de_partida == 1: # al detectar que adivinó la palabra, se procede a salir
                break
          elif detectaintentos == 5:
            cleanS() # limpieza de pantalla
            verresultado = resultado.replace(" ", "") # borrar espacios de verresultado para ser analizado
            # verificacion de si veresultado (palabra en la salida de "_" o letra) es igual a la palabra clave
            # para asi determinar que ganó el juego
            if verresultado == asignacion:
              del resultado # se borra la variable para iniciar nuevo juego
              resultado = "" # se crea la variable vacia para iniciar nuevo juego
              del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
              lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
              formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
              del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
              intentoshechos = formatearintentoslista # reasignacion de lista vacia
              detectaintentos = int(-1) # se resetea los intentos fallidos
              print("")
              c_naranja("                              Haz encontrado la palabra!")
              salir_de_partida = int(1) # descripcion ARRIBA
              del detectaintentos # se eliminan los intentos para poder jugar de nuevo
              detectaintentos = int(0) # se crea la variable para volver a jugar
              print("")
              c_cian("                            Presiona Enter para continuar...")
              input()
              cleanS()
              break # se sale de la #caja jugar
            else:
              int5() # muestra el man ahorcado segun el intento actual
              ImprimirEstado() # coloca "_ " o la letra de acuerdo a la palabra clave
              Intento5() # se hace previa validación de la letra, se agrega la letra digitada a la lista de
              #            los intentos, se une la lista de los intentos en una palabra para poder se usada
              #            para recorrerse y asi mostrar alguna letra que esté en la palabra clave
              if salir_de_partida == 1: # al detectar que adivinó la palabra, se procede a salir
                break
          elif detectaintentos == 6: # al finalizar todos los intentos, se procede a dar mensaje
            cleanS()
            int6()
            transformarAsigAMayus = asignacion.upper() # se usa para transformar la palabra clave a mayúsculas
            os.system("echo "+"'"+"\e[34m"+"                          Haz perdido, la palabra era: "+"\e[35m"+transformarAsigAMayus+"\e[0m"+"'")
            del transformarAsigAMayus # se elimina para limpiar la información
            transformarAsigAMayus = "" # se resetea para nuevo uso
            print("")
            c_cian("                           Presiona Enter para continuar")
            input()
            del detectaintentos # se eliminan los intentos para poder jugar de nuevo
            detectaintentos = int(0) # se crea la variable para volver a jugar
            del resultado # se borra la variable para iniciar nuevo juego
            resultado = "" # se crea la variable vacia para iniciar nuevo juego
            del lista_intentos_unida_en_palabra # se borra la variable de la union de los intentos
            lista_intentos_unida_en_palabra = "" # se crea la variable de la unios de los intentos
            formatearintentoslista = intentoshechos # borrar contenido de la lista y reemplazar por lista vacia
            del intentoshechos[:] # se elimina el contenido de la lista de los intentos registrados
            intentoshechos = formatearintentoslista # reasignacion de lista vacia
            cleanS()
            break
# ingreso menu 2, agregar palabras clave
      elif op == "2":
        cleanS()
        MensajeBienvenido()
        print("")
        c_azul("Digite la palabra clave y presiona Enter")
        while(True): # caja para validar la palabra a guardar
          print("")
          word = input()
          if len(word) <= 1:
            cleanS()
            MensajeBienvenido()
            print("")
            c_rojoalerta("Digite una palabra válida sin números y sin espacios!")
          else:
            transformador = list(word)
            for verify in transformador:
              if verify in '1234567890 ':
                test4 = int(1)
            if test4 == 1:
              cleanS()
              MensajeBienvenido()
              print("")
              c_rojoalerta("Digite una palabra válida sin números y sin espacios!")
              test4 = int(0) # Reseteo de testigo
            else:
              wordc = word.strip()
              Reg_palabras(wordc)
              break
# ingreso a listar palabras menu 2
      elif op == "3":
        cleanS()
        MensajeBienvenido()
        print("")
        listanum = int(1) # contador
        for i in palabras:
          transformadorstr = str(listanum)
          os.system("echo "+"'" +"\e[33m"+"                                   Palabra "+transformadorstr+": "+"\e[35m"+i+"\e[0m"+"'")
          listanum = listanum + 1
        print("")
        c_cian("                             Presiona Enter para continuar")
        print("")
        input()
        cleanS()
# salir del menu 2
      elif op == "4":
        test2 = int(0) # reinicio de testigo
        break
# error de opcion menu 2
      else:
        cleanS()
        print("No existe la opción!")
        print("")
# menu 1, salir del juego
  elif op == "2":
    cleanS()
    break
# error de eleccion menu 1
  else:
    cleanS()
    test3 = int(1)
    print("No existe la opción")
    print("")

