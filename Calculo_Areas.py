#función de cálculo
def cal_area (opc):
    b=float(input("\nIngrese el valor de la base: "))
    h=float(input("Ingrese el valor de la altura: "))
    if opc==3:
        return(b*h)/2
    else:
        return(b*h)

#programa de Calculo de area
while True:
    print("\n<------- Sistema de Cálculo de Areas ------->\n")
    print("Elija la opción correcta\n")
    print("1 Cálculo del Area de un Rectángulo")
    print("2 Cálculo del Area de un Paralelogramo")
    print("3 Cálculo del Area de un Triángulo")
    print("4 Salir\n")
    opc=float(input("Ingrese la opción: "))
    if opc==1:
        print("\nEl valor del área del Rectángulo es: ", cal_area(opc))
    elif opc==2:
        print("\nEl valor del área del Paralelogramo es: ", cal_area(opc))
    elif opc==3:
        print("\nEl valor del área del Triángulo es: ", cal_area(opc))
    elif opc==4:
        print("\nGracias por usar el sistema\n")
        break
    else:
        print("\nOpción Incorrecta, vuelva a seleccionar")
    input("\nPresione Enter para continuar...")