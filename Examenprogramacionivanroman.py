MENU = """
Sistema de Gestion de Clinica
    1. Cargar pacientes
    2. Mostrar todos los pacientes
    3. Buscar paciente por numero de historia clinica
    4. Ordenar pacientes por numero de historia clinica
    5. Mostrar paciente con mas dias de internacion
    6. Mostrar paciente con menos dias de internacion
    7. Cantidad de pacientes con mas de 5 dias de internacion
    8. Promedio de dias de internacion de todos los pacientes
    9. Salir
"""

def mostrar_menu(MENU: str) -> None:
    """Muestra el menu de opciones disponibles para el sistema."""
    print(MENU)

def cargar_pacientes(pacientes: list) -> None:
    """Carga la información de los pacientes ingresada por el usuario."""
    cantidad = int(input("Ingrese la cantidad de pacientes a cargar: "))
    for _ in range(cantidad):
        numero_historia = int(input("Número de historia clínica: "))
        nombre = input("Nombre del paciente: ")
        edad = int(input("Edad del paciente: "))
        diagnostico = input("Diagnóstico: ")
        dias_internacion = int(input("Cantidad de días de internación: "))
        pacientes.append([numero_historia, nombre, edad, diagnostico, dias_internacion])

def mostrar_pacientes(pacientes: list) -> None:
    """Muestra todos los pacientes registrados."""
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return
    for paciente in pacientes:
        print(f"Historia clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Días de internación: {paciente[4]}")

def buscar_paciente(pacientes: list, historia_clinica: int) -> None:
    """Busca un paciente por su número de historia clínica y muestra sus datos."""
    for paciente in pacientes:
        if paciente[0] == historia_clinica:
            print(f"Historia clínica: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, Días de internación: {paciente[4]}")
            return
    print("Paciente no encontrado")

def ordenar_pacientes(pacientes: list) -> None:
    """Ordena la lista de pacientes por el número de historia clínica en orden ascendente."""
    for i in range(len(pacientes)):
        for j in range(i + 1, len(pacientes)):
            if pacientes[i][0] > pacientes[j][0]:
                pacientes[i], pacientes[j] = pacientes[j], pacientes[i]

def paciente_mas_dias(pacientes: list) -> None:
    """Muestra el paciente que tiene más días de internación."""
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return
    max_paciente = pacientes[0]
    for paciente in pacientes:
        if paciente[4] > max_paciente[4]:
            max_paciente = paciente
    print(f"Paciente con más días de internación: Historia clínica: {max_paciente[0]}, Nombre: {max_paciente[1]}, Días de internación: {max_paciente[4]}")

def paciente_menos_dias(pacientes: list) -> None:
    """Muestra el paciente que tiene menos días de internación."""
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return
    min_paciente = pacientes[0]
    for paciente in pacientes:
        if paciente[4] < min_paciente[4]:
            min_paciente = paciente
    print(f"Paciente con menos días de internación: Historia clínica: {min_paciente[0]}, Nombre: {min_paciente[1]}, Días de internación: {min_paciente[4]}")

def contar_pacientes_mas_dias(pacientes: list) -> int:
    """Cuenta la cantidad de pacientes que tienen más de 5 días de internación."""
    contador = 0
    for paciente in pacientes:
        if paciente[4] > 5:
            contador += 1
    return contador

def promedio_dias_internacion(pacientes: list) -> None:
    """Calcula y muestra el promedio de días de internación de todos los pacientes."""
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
        return
    total_dias = 0
    for paciente in pacientes:
        total_dias += paciente[4]
    promedio = total_dias / len(pacientes)
    print("Promedio de días de internación:", promedio)

def ejecutar_opcion(seguir: bool, pacientes: list) -> bool:
    """
    Recibe parametro "seguir" (bool), se le pregunta un numero de opcion y ejecuta esa opcion(funcion) o finaliza el programa.
    Parametros: seguir (bool), pacientes (list)
    Salida: seguir (bool)
    """
    opcion = int(input("Elige una opcion: "))
    
    while opcion < 1 or opcion > 9: 
        print("Opcion no valida")
        opcion = int(input("Elige una opcion(1-9): "))
    
    if opcion == 1:
        cargar_pacientes(pacientes)
    elif opcion == 2:
        mostrar_pacientes(pacientes)
    elif opcion == 3:
        historia_clinica = int(input("Ingrese el número de historia clínica a buscar: "))
        buscar_paciente(pacientes, historia_clinica)
    elif opcion == 4:
        ordenar_pacientes(pacientes)
        print("Pacientes ordenados por número de historia clínica.")
    elif opcion == 5:
        paciente_mas_dias(pacientes)
    elif opcion == 6:
        paciente_menos_dias(pacientes)
    elif opcion == 7:
        cantidad = contar_pacientes_mas_dias(pacientes)
        print(f"Cantidad de pacientes con más de 5 días de internación: {cantidad}")
    elif opcion == 8:
        promedio_dias_internacion(pacientes)
    else:
        print("Saliendo del sistema.")
        return False
        
    return True

pacientes = []
seguir = True
while seguir:
    mostrar_menu(MENU)
    seguir = ejecutar_opcion(seguir, pacientes)