#Autor: Víctor Manuel Rodríguez Loyola
#Resolución de diferentes problemas utilizando el ciclo While


def dividir(dividendo, divisor): #Hace divisiones mediante restas consecutivas
    cociente = 0
    dividendoOriginal= dividendo #Para poder imprimir el dividendo original en el resultado
    while dividendo >= divisor:
        dividendo = dividendo-divisor
        cociente += 1
    print((dividendoOriginal),"/",(divisor),"=",(cociente),", Sobra",(dividendo))


def encontrarMayor(): #Imprime el mayor de una serie indefinida de números ingresados por el usuario
    print("Teclea una serie de números para encontrar el mayor.")
    numero= int(input("Teclea un número [-1 para salir]: "))
    numeroMayor= numero
    while numero !=-1:
        numero = int(input("Teclea un número [-1 para salir]: "))
        if numero>numeroMayor:
            numeroMayor=numero
    if numeroMayor==-1:
        print("No hay valor mayor.")
    else:
        print("El mayor es:", numeroMayor)


def main():
    print("Misión 07. Ciclos while ")
    print("Autor: Víctor Manuel Rodríguez Loyola")
    print("Matrícula: A01747755")
    print("1. Calcular divisiones")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion= int(input("Teclea tu opción: "))
    while opcion !=3:
        if opcion==1:
            print("Calculando divisiones")
            dividendo= int(input("Dividendo: "))
            divisor= int(input("Divisor: "))
            dividir(dividendo,divisor)
            print("\nMisión 07. Ciclos while ")
            print("Autor: Víctor Manuel Rodríguez Loyola")
            print("Matrícula: A01747755")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opcion = int(input("Teclea tu opción: "))
        elif opcion==2:
            encontrarMayor()
            print("\nMisión 07. Ciclos while ")
            print("Autor: Víctor Manuel Rodríguez Loyola")
            print("Matrícula: A01747755")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opcion = int(input("Teclea tu opción: "))
        elif opcion <1 or opcion>3:
            print("ERROR, teclea 1, 2 o 3.")
            print("\nMisión 07. Ciclos while ")
            print("Autor: Víctor Manuel Rodríguez Loyola")
            print("Matrícula: A01747755")
            print("1. Calcular divisiones")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opcion = int(input("Teclea tu opción: "))
    print("Gracias por usar este programa. Regresa pronto.")


main()