# TALLER PRACTICO GIT Y GITHUB

# SEMILLERO SEKIA

# PROGRAMA DE TASA DE CONVERSION

 

# 1. Definición y análisis del problema

# Convertir una suma de dinero a su tasa de cambio con una comision

 

# 2. Diseño del programa

# - Obtener el monto a tratar

# - Escoger una tasa de cambio

# - Imprimir resultado con la comision correspondiente

# - Tener en cuenta validaciones

 

# 3. Implementación

 

# Obtener el monto a tratar:

 

while True:

    valor = input("Inserte la cantidad de dinero en COP: ")

   

    try:

        valor = float(valor)

       

    except ValueError:

        print("El valor no es de tipo int o float, el programa terminará")

        break

   

# Escoger una tasa de cambio

 

    print("Desea cambiar el valor por: ")

    moneda = input("USD = 1 / JPY = 2 / EUR = 3:\n")

    resultado = 0

 

# Imprimir el resultado con la comision correspondiente

 

    try:

        moneda = int(moneda)

        if moneda == 1:

            resultado = valor * 0.00028

            print("El resultado en USD es de: "+str(resultado))

            print("La casa de cambio recibe: "+str(resultado*0.02)+" del valor en USD")

        elif moneda == 2:

            resultado = valor * 0.029

            print("El resultado en JPY es de: "+str(resultado))

            print("La casa de cambio recibe: "+str(resultado*0.02)+" del valor en JPY")

        elif moneda == 3:

            resultado = valor * 0.00023

            print("El resultado en EUR es de: "+str(resultado))

            print("La casa de cambio recibe: "+str(resultado*0.02)+" del valor en EUR")

        else:

            print("No se ingreso un numero valido, el programa terminará")

            break

   

    except ValueError:

        print("El valor no es de tipo int o float, el programa terminará")

 

    # Imprimir otro valor

 

    opc = input("Desea ingresar otro valor(S/N): ")

   

    if opc == "S" or opc == "s":

        continue

    elif opc == "N" or opc == "n":

        break

    else:

        print("No se ha ingresado un valor valido, el programa terminará")

        break

               

# 4. Pruebas y mantenimiento

# - El programa valida las entradas numericas

# - El programa permite la posibiidad de realizar varias conversiones

# - El programa cuenta con salidas o terminaciones del programa en casos

# previstos

# - Se verifica la formula a mano

# - Se tiene en cuenta la comision de la casa de cambio