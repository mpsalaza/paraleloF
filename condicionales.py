
"""edad = int(input("Ingresa la edad:" ))
if edad >= 18:
    print("Eres mayor de edad.")
else:
     print("Eres menor de edad.")"""
    

a = 2
b = 2
if (a == b):
 print ('a = b')
 print ('son iguales')
else: 
 print('son diferentes')




#ejercicio #2
"""numero = int(input("Ingresa un número: "))

if (numero % 2 == 0):
    print("El número es par.")
else:
    print("El número es impar.")


#ejercicio #3

usuario = input("Ingresa tu usuario: ")
contraseña = input("Ingresa tu contraseña: ")

if usuario == "admin":
    if contraseña == "1234":
        print("Acceso concedido.")
    else:
        print("Contraseña incorrecta.")
else:
    print("Usuario no reconocido.")"""



#ejercicio 

"""temperatura = float(input("Ingresa la temperatura en °C: "))

if temperatura < 10:
    print("Hace mucho frío.")
elif 10 <= temperatura <= 25:
    print("El clima es agradable.")
else:
    print("Hace calor.")"""
# comparar si los numeros son iguales 
"""a = 7
b = 7
c = 5
if (a == b):
    if (b == c):
        print ('a = b = c')
        print ('a, b y c son iguales')
    else:
        print ('a = b pero b y c son diferentes')
else:
    print ('a y b son diferentes')

#Determinar si un número es positivo, negativo o cero


""num = float(input("Ingresa un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")""


# Determinar el mayor de tres números
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a > b and a > c:
    print(f"El número mayor es: {a}")
elif b > a and b > c:
    print(f"El número mayor es: {b}")
else:
    print(f"El número mayor es: {c}")


# ejercicios con errores

edad = int(input("Ingresa tu edad: "))
if edad >= 18:
print("Eres mayor de edad.")
else:
print("Eres menor de edad.")

#Falta de indentación en las líneas dentro del if y else.

#correcto
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")"""

"""a = 0
if (a>0):
    print('a > 0')
elif(a<0):
    print ('a < 0')
else:
   print ('a = 0')"""


"""edad = int(input("Ingresa tu edad: "))

if edad <= 18:
    print("Eres menor de edad.")
elif edad <= 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")"""


"""numero = float(input("Ingresa un número: "))
if (numero>0):
    print("El numero es positivo")
elif (numero<0):
    print ("El numero es negativo")
else:
    print("El numero es cero")"""



# Solicita al usuario que ingrese su edad
"""edad = int(input("Ingresa tu edad: "))

# Clasifica la edad en categorías
if 1 <= edad <= 12:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif 18 <= edad <= 64:
    print("Eres un adulto.")
elif 65 <= edad <= 100:
    print("Eres un adulto mayor.")
elif edad < 1:
    print("edad no válida.")
else:
    print("Edad no válida.")"""
    

"""calificacion = float(input("Ingresa la calificación (0-100): "))

# Clasifica la calificación en letras
if 90 <= calificacion <= 100:
    print("Calificación: A")
elif 80 <= calificacion < 90:
    print("Calificación: B")
elif 70 <= calificacion < 80:
    print("Calificación: C")
elif 60 <= calificacion < 70:
    print("Calificación: D")
elif 0 <= calificacion < 60:
    print("Calificación: F")
else:
    print("Calificación no válida.")"""

