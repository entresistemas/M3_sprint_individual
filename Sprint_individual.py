import random
import string

nombres = ["Juan", "Diego", "Bastián", "Ingrid", "Luna", "Martin", "Agustina", "Denis", "Mohammed", "Daniel"]

# Definir una función que cree una contraseña aleatoria con letras mayúsculas, minúsculas y números
def crear_contraseña():
    caracteres = string.ascii_letters + string.digits
    contraseña = "".join(random.choice(caracteres) for i in range(8))
    return contraseña

# Crear un diccionario para almacenar las contraseñas y los números de teléfono
usuarios = {}

# Solicitar un número de teléfono válido para cada persona y crear una contraseña aleatoria para cada una
for nombre in nombres:
    telefono = input("Ingresa el número de teléfono para " + nombre + ": ")
    while len(telefono) != 8 or not telefono.isdigit():
        telefono = input("Número de teléfono inválido. Por favor, ingresa un número de teléfono de 8 dígitos: ")
    contraseña = crear_contraseña()
    usuarios[nombre] = {"contraseña": contraseña, "teléfono": telefono}

# Imprimir el diccionario con las contraseñas y los números de teléfono
print(usuarios)


