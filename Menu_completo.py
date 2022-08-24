import datetime
ahora = datetime.datetime.now()
#print(ahora)
#print(type(ahora))



print('                                         ')
print(' **** Bienvenido al sistema de MENU  ****')
print('                                         ')
print(ahora.strftime('             %d/%m/%Y %H:%M'           ))

nombre = input("             Escriba su nombre: ")
print ("gracias por estar en nuestro sistema "+ nombre)
clave = int(input("          Escriba su clave: "))


if clave == 123:


    print("Por favor elija una opcion del menu")
    print("1 - suma")
    print("2 - Resta")
    print("3 - salir")
    op1 = int(input("Cual es tu opcion: "))
    while (op1!= 0):

        if op1 == 1:
            Num1 = input("Cual es tu primer valor? ")
            Num1 = int(Num1)
            Num2 = input("Cual es tu segundo valor? ")
            Num2 = int(Num2)
            resu = Num1 + Num2
            #resu = round(resu, 2)
            resu = str(resu)
            print("resultador de tu suma: " + resu + " Soy el mejor" )
            
            
            
        elif op1 == 2:
            Num1 = input("Cual es tu primer valor? ")
            Num1 = float(Num1)
            Num2 = input("Cual es tu segundo valor? ")
            Num2 = float(Num2)
            resu = Num1 - Num2
            resu = round(resu, 2)
            resu = str(resu)
            print("resultador de tu resta: " + resu + " Soy el mejor" )
            
        elif op1 == 3:
            print(' **** Saliendo del menu  ****')
            break

            
           

        else:
            print("incorrecto")

        print(" ")
        print("Elija una opcion")
        print("1 - suma")
        print("2 - Resta")
        print("3 - salir")
        op1 = int(input("Cual es tu opcion: "))

    
        
else:
    print("CONTRASENA INCORRECTA")

