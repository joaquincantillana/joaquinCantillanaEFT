def mostrar_menu():
    print("--Menu principal--")
    print("1. Cupos por genero")
    print("2. Busqueda de peliculas por rango de precio")
    print("3. Actualizar precio de pelicula")
    print("4. Agregar pelicula")
    print("5. Eliminar pelicula")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            op = int(input("Ingrese opcion: "))
            if op < 1 or op > 6:
                print("debe de seleccionar una opcion dentro del menu")
            else:
                break
        except ValueError:
            print("tiene que ser un numero")
    return op

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_idioma(idioma):
    return idioma.strip() != ""

def validar_clasificacion(clasificacion):
    clasificacion = clasificacion.upper().strip()
    
    return clasificacion == "A" or clasificacion == "B" or clasificacion == "C"


def validar_duracion_min(duracion):
    try:
        duracion = int(duracion)
        return duracion > 0 
    except ValueError:
        return True

def validar_es_3d(formato):
    formato = formato.lower().strip()
    
    return formato == "s" or formato == "n"

def validar_precio(precio):
    try:
        precio = int(precio)
        return precio > 0 
    except ValueError:
        return False
    
def validar_cupos(cupos):
    try:
        cupos = int(cupos)
        return cupos >= 0 
    except ValueError:
        return False


peliculas = {
    "P101":["Luz de Otoño", "drama", "110", "B", "Español", False],
    "P102":["Noche neon", "accion", "125", "C", "Ingles", True],
    "P103":["Planeta Agua", "documental", "90", "A", "Español", False],
    "P104":["Risa Total", "comedia", "105", "A", "Español", True],
    "P105":["Codigo Zero", "thriller", "118", "C", "Ingles", True],
    "P106":["Viaje Lunar", "ciencia ficcion", "132", "B", "Ingles", False],
    
    }

cartelera = {
    "P101": [5990, 40],
    "P102": [7990, 0],
    "P103": [4990, 25],
    "P104": [6990, 12],
    "P105": [8990, 8],
    "P106": [7490, 3],
                    
    
    }

def cupos_genero(genero, cartelera, peliculas):
    total = 0 
    for codigo in peliculas:
        datos = peliculas[codigo]
        if datos[1].lower() == genero.lower():
            total += cartelera[codigo][1]
    print(f"el total de cupos es: {total}")
    
            

def eliminar_codigo(codigo, cartelera, peliculas):
    correcto = buscar_codigo(codigo, cartelera)
    if correcto:
        del cartelera[codigo.upper()]
        del peliculas[codigo.upper()]
        return True
    return False
    

def busqueda_precio(p_min, p_max, cartelera, peliculas):
    lista = []
    for codigo in cartelera:
        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]
        if precio >= p_min and precio <= p_max and cupos != 0:
            titulo = peliculas[codigo][0]
            lista.append(f"{titulo}-{codigo}")
    if len(lista) == 0:
        print("ese codigo no existe")
    else:
        lista.sort()
        print(lista)
                         

def buscar_codigo(codigo, cartelera):
    codigo = codigo.upper()
    return codigo in cartelera

def actualizar_precio(codigo, nuevo_precio, cartelera):
    correcto = buscar_codigo(codigo, cartelera)
    if correcto:
        cartelera[codigo.upper()][0] = nuevo_precio
        return True
    return False



def validar_codigo(codigo, pelicula):
    if codigo.strip() == "":
        return False
    if codigo.upper() in pelicula:
        return False
    return True

    
def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    correcto = buscar_codigo(codigo, cartelera)
    if correcto:
        return False
    peliculas[codigo.upper()] = [
        titulo.strip(),
        genero.strip(),
        idioma.strip(),
        clasificacion.lower(),
        es_3d
        ]

    cartelera[codigo.upper()] = [
        precio,
        cupos
        ]
    return True

 
op = 0
while op != 6:
    mostrar_menu()
    op = leer_opcion()
    if op == 1:
        genero = input("Ingrese genero a consultar: ")

        cupos_genero(genero, cartelera, peliculas)
        
    elif op == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio minimo: "))
                p_max = int(input("Ingrese precio maximo: "))
                break
            except ValueError:
                print("debe de ingresar valores enteros")
        busqueda_precio(p_min, p_max, cartelera, peliculas)

    elif op == 3:
        otra = "s"
        while otra == "s":
            codigo = input("ingrese codigo de pelicula: ")
            while True:
                precio = input("ingrese nuevo precio: ")
                correcto = validar_precio(precio)
                if correcto:
                    precio = int(precio)
                    break
                else:
                    print("debe de ingresar un entero positivo")
            correcto = actualizar_precio(codigo, precio, cartelera)
            if correcto:
                print("precio actualizado")
            else:
                print("el codigo no existe")
            otra = input("¿Desea actualizar otro precio?:  (s/n)").lower()
            

    elif op == 4:
        codigo = input ("ingrese codigo de pelicula: ")
        correcto = validar_codigo(codigo, cartelera)
        if not correcto:
            print("el codigo no existe")
        else:
            titulo = input("Ingrese titulo: ")
            correcto = validar_titulo(titulo)
            if not correcto:
                print("titulo incorrecto ")
            else:
                genero = input("Ingrese genero: ")
                correcto = validar_genero(genero)
                if not correcto:
                    print("genero incorrecto ")
                else:
                    duracion = input("Ingrese duracion (minutos): ")
                    correcto = validar_duracion_min(duracion)
                    if not correcto:
                        print("duracion incorrecta ")
                    else:
                        clasificacion = input("Ingrese clasificacion: ")
                        correcto = validar_clasificacion(clasificacion)
                        if not correcto:
                            print("clasificacion incorrecta ")
                        else:
                            idioma = input("Ingrese idioma : ")
                            correcto = validar_idioma(idioma)
                            if not correcto:
                                print("idioma incorrecto ")
                            else:
                                formato = input("¿es 3D ?(s/n): ")
                                correcto = validar_es_3d(formato)
                                if not correcto:
                                    print("dato incorrecto ")
                                else:
                                    precio = input("Ingrese precio: ")
                                    correcto = validar_precio(precio)
                                    if not correcto:
                                        print("precio incorrecto ")
                                    else:
                                        cupos = input("Ingrese cupos: ")
                                        correcto = validar_cupos(cupos)
                                        if not correcto:
                                            print("cupos incorrectos ")
                                        else:
                                            formato = formato.lower() == "s"
                                            precio = int(precio)
                                            cupos = int(cupos)
                                            correcto = agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, formato, precio, cupos)
                                            if correcto:
                                                print("pelicula agregada")
                                            else:
                                                print("el codigo ya existe")
                                        
                            
                        

    elif op == 5:
        codigo = input ("ingrese el codigo: ")
        correcto = eliminar_codigo(codigo, cartelera, peliculas)
        if correcto:
            print("Pelicula eliminada")
        else:
            print("el codigo no existe")
        
    elif op == 6:
        print("Programa finalizado.")

    


