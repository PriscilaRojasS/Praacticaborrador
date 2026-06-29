import os
nombre = os.environ.get("NOMBRE", 'Mundo')

print(f"Hola {nombre}! Mi app funciona en Docker .")
print("Version 1.0")