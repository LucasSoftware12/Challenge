# Alumno Lucas Medina

'''
Ejercicio 1:
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
'''
# Coloque la resolución del Ejercicio debajo de esta línea
palabra = input('\nIngrese una palabra: ')

vocales = ["a", "e", "i", "o", "u"]

for i in vocales:
    contador = 0
    for letra in palabra:
        if letra == i:
            contador += 1
    print(f"La vocal '{i}' aparece {contador} veces")

'''
Ejercicio 2:
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
'''
# Coloque la resolución del Ejercicio debajo de esta línea
inicio = True
listaVacia = []

while inicio:
    palabras = input('\nIngrese una palabra: ')
    listaVacia.append(palabras)
    seguimos = int(input('\n¿Quiere seguir agregando palabras? '
                         '\n1= Si''\n0= No'
                         '\n : '))
    if seguimos == 0:
        inicio = False

nuevaPalabraUno = input('Ingrese la palabra para sustituir: ')
nuevaPalabraDos = input('Ingrese otra palabra: ')
listaVacia.append(nuevaPalabraDos)

listaVacia[1] = nuevaPalabraUno
print(listaVacia)
