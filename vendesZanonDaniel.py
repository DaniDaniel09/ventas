# Daniel Zanón López

productos = []
precios = []
cVendidas = []

while True:

    print("""
    0. Asignar valores por defecto
    1. Introducir un articulo nuevo
    2. Hacer una venta
    3. Mostrar informacion.
    4. Eliminar un articulo
    5. Eliminar todos los articulos
    6. Salir
    """)

    opcion = int(input())
    if opcion == 0:
        productos.extend(["raton","teclado","monitor"])
        precios.extend([10,15,120])
        cVendidas.extend([10,10,5])
    elif opcion == 1:
        producto = None
        precio = 0

        producto = input("Producto: ")
        productos.append(producto)
        precio = float(input("Precio: "))
        precios.append(precio)
        cVendidas.append(0)
    elif opcion == 2:
        productoEncontrado = False
        productoBusqueda = None
        unidades = 0

        productoBusqueda = input("¿Cual es el producto? ")
        for i in range (len(productos)):
            if productos[i] == productoBusqueda:
                unidades = int(input("¿Cuantas unidades has vendido? "))
                cVendidas[i] = unidades
                productoEncontrado = True
                break
        if productoEncontrado == False:
            print("No se ha encontrado el producto")
    elif opcion == 3:
        cantAnt = 0
        impAnt = 0
        nombreCantMax = None
        nombreImpMax = None
        importe = 0
        importeTotal = 0

        print("NOMBRE".ljust(10, ' '), "CANT".rjust(10, ' '), "PRECIO".rjust(10,' '), "IMPORTE".rjust(10, ' '))
        for i in range (len(productos)):
            importe = cVendidas[i]*precios[i]
            importeTotal += importe
            print(productos[i].ljust(10, ' '),"%10s %10.2f %10.2f"%(cVendidas[i],precios[i], importe))
            if importe > impAnt:
                nombreImpMax = productos[i]
                impMax = importe
            if cVendidas[i] > cantAnt:
                nombreCantMax = productos[i]
                cantMax = cVendidas[i]
            impAnt = importe
            cantAnt = cVendidas[i]
        print(""

        "")
        print("TOTAL:".rjust(30, " "),"%12.2f"%(importeTotal))
        print(""

        "")
        print("Articulo mas vendido:",nombreCantMax,", con", cantMax,"unidades.")
        print("Articulo con mas ingresos:",nombreImpMax,", con", impMax,"euros.")
    elif opcion == 4:
        posicionProducto = int(input("¿Que producto quieres borrar? "))
        productos.pop(posicionProducto)
        precios.pop(posicionProducto)
        cVendidas.pop(posicionProducto)
        print("El producto ha sido eliminado correctamente.")
    elif opcion == 5:
        productos.clear()
        precios.clear()
        cVendidas.clear()
        print("Todo ha sido eliminado correctamente.")
    elif opcion == 6:
        sn = None

        sn = input("¿Quieres salir (s/n)? ")
        if sn == "s":
            break
    else:
        print("Opcion no disponible.")