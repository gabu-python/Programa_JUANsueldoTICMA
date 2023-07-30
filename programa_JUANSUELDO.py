# Definir los sueldos mensuales de Juan
def calcular_sueldo_promedio():
    sueldos = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]

    # Calculo del sueldo promedio
    sueldo_promedio = sum(sueldos) / len(sueldos)
    return sueldo_promedio

# Definir los rangos de categorías de sueldo


def determinar_categoria_sueldo(sueldo_promedio):
    sueldo_bajo = 300
    sueldo_normal = 900

    # Determinar en qué categoría se encuentra el sueldo promedio
    if sueldo_promedio < sueldo_bajo:
        return "Sueldo bajo"
    elif sueldo_bajo <= sueldo_promedio <= sueldo_normal:
        return "Sueldo normal"
    else:
        return "Sueldo mejor de lo normal"


# Llamar a las funciones para obtener los resultados
sueldo_promedio_juan = calcular_sueldo_promedio()
categoria_sueldo_juan = determinar_categoria_sueldo(sueldo_promedio_juan)

# Mostrar los resultados
print("Sueldo promedio de Juan: ${:.2f}".format(sueldo_promedio_juan))
print("Categoría de sueldo de Juan:", categoria_sueldo_juan)
