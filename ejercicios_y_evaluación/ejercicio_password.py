import re

def evaluar_contrasena(contrasena):
    puntaje = 0
    criterios = []

    # Longitud de la contraseña
    if len(contrasena) >= 12:
        puntaje += 2
        criterios.append("✔️ Longitud adecuada (12+ caracteres)")
    elif len(contrasena) >= 8:
        puntaje += 1
        criterios.append("✔️ Longitud mínima alcanzada (8-11 caracteres)")
    else:
        criterios.append("❌ Contraseña demasiado corta")

    # Letras mayúsculas y minúsculas
    if any(c.islower() for c in contrasena) and any(c.isupper() for c in contrasena):
        puntaje += 2
        criterios.append("✔️ Contiene mayúsculas y minúsculas")
    else:
        criterios.append("❌ Faltan mayúsculas o minúsculas")

    # Números
    if any(c.isdigit() for c in contrasena):
        puntaje += 1
        criterios.append("✔️ Contiene números")
    else:
        criterios.append("❌ No contiene números")

    # Caracteres especiales
    if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in contrasena):
        puntaje += 2
        criterios.append("✔️ Incluye caracteres especiales")
    else:
        criterios.append("❌ No incluye caracteres especiales")

    # Evitar palabras comunes
    palabras_comunes = ["password", "123456", "qwerty", "admin", "welcome"]
    if any(palabra in contrasena.lower() for palabra in palabras_comunes):
        criterios.append("❌ Contiene palabras comunes (ej. 'password', '123456')")
    else:
        puntaje += 2
        criterios.append("✔️ No contiene palabras comunes")

    return puntaje, criterios

def main():
    print("Bienvenido al evaluador de contraseñas.")
    print("Introduce una contraseña para evaluar su seguridad:")
    contrasena = input("Contraseña: ")

    puntaje, criterios = evaluar_contrasena(contrasena)

    print("\nEvaluación de la contraseña:")
    for criterio in criterios:
        print(f" - {criterio}")

    print(f"\nPuntaje total: {puntaje}/9")
    if puntaje < 5:
        print("❌ La contraseña es débil. ¡Mejora tu contraseña!")
    elif puntaje < 8:
        print("⚠️ La contraseña es moderada. Considera reforzarla.")
    else:
        print("✔️ La contraseña es fuerte. ¡Buen trabajo!")

if __name__ == "__main__":
    main()
