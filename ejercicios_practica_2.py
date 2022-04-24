# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
   # archivo = 'stock.csv' (!!Tuve que comentar esta línea, y pasar el path completo para que encontrara el archivo, como sigue:)
    archivo = '/home/karol/Documents/Cursos/Inove_Python Developer/I_Py Inicial/M6_archivos/archivos_python/stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    csvfile = open(archivo)
    stock_inicial = list(csv.DictReader(csvfile)) #genero una lista donde cada elemento es un diccionario
    
    suma_tornillos = 0

    for producto in stock_inicial:
        cantidad_fila = int(producto['tornillos'])
        suma_tornillos += cantidad_fila
    print('Total de tornillos: ', suma_tornillos)

    csvfile.close()


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'
    
    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    with open('/home/karol/Documents/Cursos/Inove_Python Developer/I_Py Inicial/M6_archivos/archivos_python/propiedades.csv') as csvfile:
        datos = list(csv.DictReader(csvfile)) #genero una lista donde cada elemento es un diccionario 

        deptos_2amb = 0
        deptos_3amb = 0

        for i in range(len(datos)): 
            try:
                ambientes = int(datos[i].get('ambientes'))
                if ambientes == 2:
                    deptos_2amb += 1

                elif ambientes == 3:
                    deptos_3amb +=1    

            except:
                print('Dato faltante o erróneo para cantidad de ambientes, en fila',i+1)    

        print('Total departamentos de 2 ambientes:',deptos_2amb)
        print('Total departamentos de 3 ambientes:',deptos_3amb)






if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
