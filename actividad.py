def solicitar_binario(mensaje):
    """Solicita y valida que la cadena ingresada contenga únicamente '0' y '1'."""
    while True:
        entrada = input(mensaje).strip()
        if entrada and all(c in '01' for c in entrada):
            return entrada
        print("  [Error] Ingresa únicamente dígitos binarios válidos (0 y 1).")

def solicitar_octal(mensaje):
    """Solicita y valida que la cadena ingresada contenga dígitos del '0' al '7'."""
    while True:
        entrada = input(mensaje).strip()
        if entrada and all(c in '01234567' for c in entrada):
            return entrada
        print("  [Error] Ingresa únicamente dígitos octales válidos (0 al 7).")

def solicitar_hexadecimal(mensaje):
    """Solicita y valida que la cadena contenga dígitos de '0'-'9' y 'A'-'F'."""
    while True:
        entrada = input(mensaje).strip().upper()
        if entrada and all(c in '0123456789ABCDEF' for c in entrada):
            return entrada
        print("  [Error] Ingresa únicamente caracteres hexadecimales válidos (0-9 y A-F).")


# Convertir

def op1_binario_a_octal():
    print("\n 1. Convertir de Binario a Octal ")
    binario = solicitar_binario("Ingresa un número en base binaria (Base 2): ")
    # Convertimos de base 2 a entero decimal, y luego a octal (quitando el prefijo '0o')
    decimal = int(binario, 2)
    octal = oct(decimal)[2:]
    print(f"-> Entrada (Base 2 - Binario): {binario}")
    print(f"-> Resultado (Base 8 - Octal): {octal}")

def op2_binario_a_hexadecimal():
    print("\n 2. Convertir de Binario a Hexadecimal ")
    binario = solicitar_binario("Ingresa un número en base binaria (Base 2): ")
    # Convertimos de base 2 a decimal, y luego a hexadecimal en mayúsculas (sin prefijo '0x')
    decimal = int(binario, 2)
    hexadecimal = hex(decimal)[2:].upper()
    print(f"-> Entrada (Base 2 - Binario):       {binario}")
    print(f"-> Resultado (Base 16 - Hexadecimal): {hexadecimal}")

def op3_octal_a_hexadecimal():
    print("\n 3. Convertir de Octal a Hexadecimal ")
    octal = solicitar_octal("Ingresa un número en base octal (Base 8): ")
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)[2:].upper()
    print(f"-> Entrada (Base 8 - Octal):          {octal}")
    print(f"-> Resultado (Base 16 - Hexadecimal): {hexadecimal}")

def op4_hexadecimal_a_octal():
    print("\n 4. Convertir de Hexadecimal a Octal ")
    hexadecimal = solicitar_hexadecimal("Ingresa un número en base hexadecimal (Base 16): ")
    decimal = int(hexadecimal, 16)
    octal = oct(decimal)[2:]
    print(f"-> Entrada (Base 16 - Hexadecimal): {hexadecimal}")
    print(f"-> Resultado (Base 8 - Octal):       {octal}")


# Suma y resta de binarios

def op5_sumar_binarios():
    print("\n  5. Sumar dos números binarios ")
    bin1 = solicitar_binario("Ingresa el primer número binario: ")
    bin2 = solicitar_binario("Ingresa el segundo número binario: ")
    
    suma_decimal = int(bin1, 2) + int(bin2, 2)
    resultado_binario = bin(suma_decimal)[2:]
    
    print(f"-> Operación: {bin1} (Base 2) + {bin2} (Base 2)")
    print(f"-> Resultado en Binario (Base 2): {resultado_binario}")

def op6_restar_binarios():
    print("\n  6. Restar dos números binarios ")
    while True:
        bin1 = solicitar_binario("Ingresa el primer número binario (minuendo): ")
        bin2 = solicitar_binario("Ingresa el segundo número binario (sustraendo): ")
        
        val1 = int(bin1, 2)
        val2 = int(bin2, 2)
        
        if val1 >= val2:
            resta_decimal = val1 - val2
            resultado_binario = bin(resta_decimal)[2:]
            print(f"-> Operación: {bin1} (Base 2) - {bin2} (Base 2)")
            print(f"-> Resultado en Binario (Base 2): {resultado_binario}")
            break
        else:
            print("  [Error] El primer número debe ser mayor o igual que el segundo. Intenta de nuevo.\n")


# Complementos a 1 y a 2

def op7_complementos():
    print("\n  7. Obtener Complemento a 1 y a 2 ---")
    while True:
        entrada = input("Ingresa un número decimal positivo entre 1 y 127: ").strip()
        if entrada.isdigit():
            numero = int(entrada)
            if 1 <= numero <= 127:
                break
        print("  [Error] Debe ser un número entero positivo dentro del rango de 1 a 127.")
    
    # 1. Convertir a binario de 8 bits rellenando con ceros a la izquierda
    binario_8bits = format(numero, '08b')
    
    # 2. Complemento a 1: invertir cada bit ('0' por '1' y '1' por '0')
    comp_a_1 = "".join('1' if bit == '0' else '0' for bit in binario_8bits)
    
    # 3. Complemento a 2: sumar 1 al complemento a 1 y mantener formato de 8 bits
    valor_comp_2 = int(comp_a_1, 2) + 1
    comp_a_2 = format(valor_comp_2, '08b')[-8:] # Asegura 8 bits exactos
    
    print(f"-> Número decimal:      {numero}")
    print(f"-> Binario (8 bits):    {binario_8bits}")
    print(f"-> Complemento a 1:     {comp_a_1}")
    print(f"-> Complemento a 2:     {comp_a_2}")


# Ascii de letras mayúsculas

def op8_ascii_mayusculas():
    print("\n--- 8. Convertir letras mayúsculas a ASCII decimal y binario ---")
    letras_validas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    while True:
        cadena = input("Ingresa una o varias letras mayúsculas (A-Z, sin acentos ni Ñ): ").strip()
        if cadena and all(letra in letras_validas for letra in cadena):
            break
        print("  [Error] Ingresa únicamente letras mayúsculas de la A a la Z (sin espacios, acentos ni Ñ).")
    
    print("\nResultados:")
    print(f"{'Letra':<8} | {'ASCII Decimal':<15} | {'Binario (8 bits)':<16}")
    print("-" * 45)
    for letra in cadena:
        codigo_ascii = ord(letra)
        binario_8bits = format(codigo_ascii, '08b')
        print(f"{letra:<8} | {codigo_ascii:<15} | {binario_8bits:<16}")


# Menu.

def mostrar_menu():
    print("  Menu principal ")
    print("1. Convertir de binario a octal.")
    print("2. Convertir de binario a hexadecimal.")
    print("3. Convertir de octal a hexadecimal.")
    print("4. Convertir de hexadecimal a octal.")
    print("5. Sumar dos números binarios.")
    print("6. Restar dos números binarios.")
    print("7. Obtener complemento a 1 y a 2.")
    print("8. Convertir letras mayúsculas a ASCII decimal y binario.")
    print("9. Salir.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-9): ").strip()
        
        if opcion == '1':
            op1_binario_a_octal()
        elif opcion == '2':
            op2_binario_a_hexadecimal()
        elif opcion == '3':
            op3_octal_a_hexadecimal()
        elif opcion == '4':
            op4_hexadecimal_a_octal()
        elif opcion == '5':
            op5_sumar_binarios()
        elif opcion == '6':
            op6_restar_binarios()
        elif opcion == '7':
            op7_complementos()
        elif opcion == '8':
            op8_ascii_mayusculas()
        elif opcion == '9':
            print("\n¡Gracias por utilizar el programa! Finalizando ejecución... ¡Hasta pronto!")
            break
        else:
            print("\n  [Error] Opción no válida. Por favor, ingresa un número del 1 al 9.")
            continue
            
        input("\nPresiona Enter para regresar al menú principal...")

if __name__ == "__main__":
    main()