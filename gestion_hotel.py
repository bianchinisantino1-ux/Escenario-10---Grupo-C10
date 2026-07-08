# ------------------------------------------------------------------
# TRABAJO FINAL INTEGRADOR - ESCENARIO 10: GESTIÓN DE HOTEL
# Comisión: C10
# ------------------------------------------------------------------

# --- VARIABLES GLOBALES (CONTADORES Y ACUMULADORES) ---
MAX_ESTANDAR = 10
MAX_PREMIUM = 5
MAX_SUITE = 3

# Habitaciones ocupadas actualmente
ocupadas_estandar = 0
ocupadas_premium = 0
ocupadas_suite = 0

# Estadísticas acumuladas
total_huespedes_atendidos = 0
total_dinero_recaudado = 0.0


# --- FUNCIONES DE VALIDACIÓN ---

def solicitar_opcion_menu():
    """Valida la opción elegida en el menú principal."""
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("[ERROR] Opción inválida. Debe ser entre 1 y 5.")
        except ValueError:
            print("[ERROR] Entrada inválida. Por favor, ingrese un número entero.")

def validar_entero_positivo(mensaje):
    """Garantiza que el usuario ingrese un número entero mayor a cero."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("[ERROR] El valor debe ser mayor a cero.")
        except ValueError:
            print("[ERROR] Entrada inválida. Ingrese un número entero.")


# --- MÓDULOS DE GESTIÓN ---

# 1. REGISTRO Y CHECK-IN
def registrar_check_in():
    global ocupadas_estandar, ocupadas_premium, ocupadas_suite, total_huespedes_atendidos
    
    print("\n--- REGISTRAR CHECK-IN DE HUÉSPED ---")
    nombre = input("Ingrese el nombre del huésped: ").strip()
    if not nombre:
        print("[ERROR] El nombre no puede estar vacío.")
        return

    print("\nSeleccione el tipo de habitación:")
    print(f"1 - Estándar ($50/noche) [Disponibles: {MAX_ESTANDAR - ocupadas_estandar}]")
    print(f"2 - Premium  ($90/noche) [Disponibles: {MAX_PREMIUM - ocupadas_premium}]")
    print(f"3 - Suite    ($150/noche) [Disponibles: {MAX_SUITE - ocupadas_suite}]")
    
    tipo = input("Seleccione opción (1-3): ")
    
    if tipo == "1":
        if ocupadas_estandar < MAX_ESTANDAR:
            ocupadas_estandar += 1
            total_huespedes_atendidos += 1
            print(f"¡[ÉXITO] Check-in completado para {nombre} en Habitación Estándar!")
        else:
            print("[ERROR] No hay habitaciones Estándar disponibles.")
            
    elif tipo == "2":
        if ocupadas_premium < MAX_PREMIUM:
            ocupadas_premium += 1
            total_huespedes_atendidos += 1
            print(f"¡[ÉXITO] Check-in completado para {nombre} en Habitación Premium!")
        else:
            print("[ERROR] No hay habitaciones Premium disponibles.")
            
    elif tipo == "3":
        if ocupadas_suite < MAX_SUITE:
            ocupadas_suite += 1
            total_huespedes_atendidos += 1
            print(f"¡[ÉXITO] Check-in completado para {nombre} en Suite!")
        else:
            print("[ERROR] No hay Suites disponibles.")
    else:
        print("[ERROR] Opción de habitación inválida.")


# 2. CONTROL DE DISPONIBILIDAD
def mostrar_estado_hotel():
    print("\n========================================")
    print("      ESTADO ACTUAL DE HABITACIONES     ")
    print("========================================")
    
    libres_estandar = MAX_ESTANDAR - ocupadas_estandar
    libres_premium = MAX_PREMIUM - ocupadas_premium
    libres_suite = MAX_SUITE - ocupadas_suite
    
    print(f"• Estándar -> Ocupadas: {ocupadas_estandar}/{MAX_ESTANDAR} | Disponibles: {libres_estandar}")
    print(f"• Premium  -> Ocupadas: {ocupadas_premium}/{MAX_PREMIUM} | Disponibles: {libres_premium}")
    print(f"• Suite    -> Ocupadas: {ocupadas_suite}/{MAX_SUITE} | Disponibles: {libres_suite}")
    print("----------------------------------------")
    
    if libres_estandar == 0 and libres_premium == 0 and libres_suite == 0:
        print("ALERTA: ¡El hotel está completamente lleno!")
    else:
        print(f"Total de habitaciones libres: {libres_estandar + libres_premium + libres_suite}")
    print("========================================")



def registrar_check_out():
    global ocupadas_estandar, ocupadas_premium, ocupadas_suite, total_dinero_recaudado
    
    print("\n--- REGISTRAR CHECK-OUT (SALIDA) ---")
    print("Seleccione el tipo de habitación a liberar:")
    print("1. Estándar")
    print("2. Premium")
    print("3. Suite")
    
    tipo = input("Opción: ")
    
    if tipo not in ["1", "2", "3"]:
        print("[ERROR] Opción inválida.")
        return
        
    noches = validar_entero_positivo("Ingrese la cantidad de noches de estadía: ")
    
    if tipo == "1":
        if ocupadas_estandar > 0:
            ocupadas_estandar -= 1
            total = noches * 50
            total_dinero_recaudado += total
            print(f"[ÉXITO] Habitación Estándar liberada. Total a pagar: ${total}")
        else:
            print("[ERROR] No hay habitaciones Estándar ocupadas actualmente.")
            
    elif tipo == "2":
        if ocupadas_premium > 0:
            ocupadas_premium -= 1
            total = noches * 90
            total_dinero_recaudado += total
            print(f"[ÉXITO] Habitación Premium liberada. Total a pagar: ${total}")
        else:
            print("[ERROR] No hay habitaciones Premium ocupadas actualmente.")
            
    elif tipo == "3":
        if ocupadas_suite > 0:
            ocupadas_suite -= 1
            total = noches * 150
            total_dinero_recaudado += total
            print(f"[ÉXITO] Suite liberada. Total a pagar: ${total}")
        else:
            print("[ERROR] No hay Suites ocupadas actualmente.")


# 4. ESTADÍSTICAS GENERALES
def mostrar_estadisticas():
    print("\n========================================")
    print("          ESTADÍSTICAS GENERALES        ")
    print("========================================")
    total_ocupadas = ocupadas_estandar + ocupadas_premium + ocupadas_suite
    total_habitaciones = MAX_ESTANDAR + MAX_PREMIUM + MAX_SUITE
    porcentaje_ocupacion = (total_ocupadas / total_habitaciones) * 100
    
    print(f"• Total de Huéspedes atendidos: {total_huespedes_atendidos}")
    print(f"• Total Recaudado en caja: ${total_dinero_recaudado}")
    print(f"• Porcentaje actual de ocupación: {porcentaje_ocupacion:.2f}%")
    print("========================================")


# --- BUCLE PRINCIPAL ---
def main():
    while True:
        print("\n========================================")
        print("    SISTEMA DE GESTIÓN HOTELERA v1.0   ")
        print("========================================")
        print("1. Registrar Huésped (Check-in)")
        print("2. Ver Estado de Habitaciones")
        print("3. Registrar Salida (Check-out)")
        print("4. Ver Estadísticas Generales")
        print("5. Salir del Sistema")
        print("========================================")
        
        opcion = solicitar_opcion_menu()
        
        if opcion == 1:
            registrar_check_in()
        elif opcion == 2:
            mostrar_estado_hotel()
        elif opcion == 3:
            registrar_check_out()
        elif opcion == 4:
            mostrar_estadisticas()
        elif opcion == 5:
            print("\n¡Gracias por utilizar el sistema! Saliendo...")
            break

if __name__ == "__main__":
    main()