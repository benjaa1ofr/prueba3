boleto=[]
asientos=[]
rut=[]
asiento_comun=60000
asiento_piernas=80000
asiento_nreclinable=50000
asientos_disponibles=(asiento_comun,asiento_piernas,asiento_nreclinable)

def comprar_pasajes():
    asiento1=0
    asiento2=0
    asiento3=0
    usuario=int(input("ingrese su cuenta rut sin n° verificador"))
    try:
        if usuario<5000000 and usuario>9999999:
            print("ah accedido correctamente")
            rut.append(usuario)
        else:
            ("no se puede ingresar el usuario")
    except ValueError:
        print("ingrese un dato valido")
    
    while True:
        print(f"(1){asiento_comun}")
        print(f"(2){asiento_piernas}")
        print(f"(3){asiento_nreclinable}")
        op=int(input("ingrese una opcion o presiona (0) para salir"))
        if op==1:
            cantidad1=int(input("ingrese la cantidad de pasajes que desea"))
            asiento1=asiento1+cantidad1
        elif op==2:
            cantidad2=int(input("ingrese la cantidad de pasajes que desea"))
            asiento2=asiento2+cantidad2
        elif op==3:
            cantidad3=int(input("ingrese la cantidad de pasajes que desea"))
            asiento3=asiento3+cantidad3
        elif op==0:
            break
        precio1=asiento_comun*asiento1
        precio2=asiento_piernas*asiento2
        precio3=asiento_nreclinable*asiento3
        total=precio1+precio2+precio3
        cantidad=asiento1+asiento2+asiento3
        pasajes=[usuario,asiento_comun, asiento_piernas, asiento_nreclinable, asiento1, asiento2, asiento3, cantidad, precio1,precio2,precio3,total]
        boleto.append(pasajes)
        
def listado_pasajeros():
    print("listado de pasajeros")
    for i in (len(rut)):
        print(i, rut[i])

def buscar_pasajero():
    usuario=input("ingrese su cuenta rut sin n° verificador")
    try:
        if usuario<5000000 and usuario>9999999:
            print("ah accedido correctamente")
        else:
            ("no se puede ingresar el usuario")
    except ValueError:
        print("ingrese un dato valido")
        if usuario in rut:
            print("datos del usuario")
            print(usuario)





while True:
    print("(1)comprar pasaje")
    print("(2)listado pasajeros")
    print("(3)buscar pasajero")
    print("(0)salir")
    opcion=int(input("ingrese una opcion"))
    if opcion==1:
        comprar_pasajes()
    elif opcion==2:
        listado_pasajeros
    elif opcion==3:
        buscar_pasajero
    elif opcion==0:
        break
        


