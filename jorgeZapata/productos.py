import os
import time
import math
import statistics
import random
from globales import seleccionar_opcion,leer_archivo_json,guardar_archivo_json



productos = [
"Café Americano",
"Té Chai",
"Croissant",
"Jugo Naranja",
"Panini de Pavo y Queso",
"Pastel de Zanahoria",
"Espresso Doble",
"Ba;do de Frutas",
"Muffin",
"Ensalada",
"Chocolate Caliente",
"Tarta de Frambuesa",
"Sándwich de Huevo",
"Galletas de Avena",
"Frappé de Caramelo"
]

def asignar():
    valorp = []
    for producto in productos:
        venta = random.uniform(2000,10000)
        valorp.append({"nombre": producto, "valor":venta})
    return valorp

def estadistica(valorp):
    if not valorp:
        print("NO HAY MONTOS QUE MOSTRAR")
        return
    valor = [valorps["valor"]for valorps in valorp ]
    valor_max = max(valor)
    valor_min = min(valor)
    promedio = statistics.mean(valor)
    media_geometrica = math.exp(math.fsum(math.log(v)for v in valor) / len(valor))
    print(f"El monto mas alto: ${valor_max:.0f}")
    print(f"El moton mas bajo: ${valor_min: .0f}")
    print(f"El promedio de valor de los productos es: ${promedio: .0f}")
    print(f"La media geometrica es: ${media_geometrica}")


def menu():
    valorp = []
    while True:
        print("=== Menu ===")
        print("1.Asignar Monto aleatorio")
        print("2.Ver Estadisticas")
        print("3.Salir del programa")
        opcion = seleccionar_opcion(3)
        if opcion < 1 or opcion > 3:
            print("opcion no valida")
        elif opcion == 1:
            valorp = asignar()
            guardar_archivo_json("venta.json",valorp)
            print("Montos aleatorios asignados")
        elif opcion == 2:
            valorp = leer_archivo_json("venta.json")
            if valorp:
                estadistica(valorp)
            print("viendo estadistica")
        elif opcion == 3:
            print("Saliendo")
            break


if __name__ == "__main__":
    menu()