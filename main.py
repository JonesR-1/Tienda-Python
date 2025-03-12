nombreVendedor=None
productos=[]
producto={}

opcion=100

print("Mercado")
print("**********")
print("1. Crear lista de mercado")
print("2. Ver lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("Presiona 5 para salir")
while opcion != 5:
    opcion=int(input("Digita una opción: "))
    if opcion == 1:
        print("Bienvenido a la creación de tu lista de mercado")

        #Creando claves y valores de un diccionario
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["precio"]=int(input("Digita el precio del producto: "))
        producto["cantidad"]=int(input("Cuantos elementos de este producto vas a llevar: "))
        producto["presentacion"]=input("¿Cual presentación llevaras? ")

        #mostrando mi diccionario
        #print(producto)

        #poblando una lista (agregando elementos a una lista)
        productos.append(producto)
        print(productos)


    elif opcion == 2:

        #Utilizando ciclos FOR en python para recorrer LISTAS

        for productoSeleccionado in productos:
            print(productoSeleccionado["nombre"])

    elif opcion == 3:

        #0. Preguntar a quien quiero editar
        productoCambio=int(input("Digita el ID del producto a cambiar: "))
        #1. Encontrar el elemento
        for productoBuscado in productos:
            if productoBuscado["id"] == productoCambio:
                print("OE lo encontre")
            else: 
                print("Parce no lo encontre")
        #2. Seleccionar el elemento
        #3. Accedo a las propiedad o atributos quiero o puedo modificar

        print("Estoy en la 3")
    elif opcion == 4:
        print("Estoy en la 4")
    else:
        print("Opción no válida")