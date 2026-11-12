import tkinter as tk
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

APP_USER = os.getenv("APP_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")


# Función 1: Capturar las credenciales
def capturar_credenciales():
	usuario = entrada_usuario.get()
	contraseña = entrada_password.get()

	validar_credenciales(usuario, contraseña)


# Función 2: Validar las credenciales
def validar_credenciales(usuario, contraseña):
	if usuario == APP_USER and contraseña == APP_PASSWORD:
		mostrar_mensaje("Acceso correcto", "green")
	else:
		mostrar_mensaje("Usuario o contraseña incorrectos", "red")


# Función 3: Mostrar el mensaje
def mostrar_mensaje(mensaje, color):
	resultado.config(text=mensaje, fg=color)


# Crear la ventana
ventana = tk.Tk()
ventana.title("Validación de credenciales")
ventana.geometry("400x350")

# Título
titulo = tk.Label(ventana, text="Iniciar sesión", font=("Arial", 18))
titulo.pack(pady=15)

# Campo de usuario
etiqueta_usuario = tk.Label(ventana, text="Usuario:")
etiqueta_usuario.pack()

entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack(pady=5)

# Campo de contraseña
etiqueta_password = tk.Label(ventana, text="Contraseña:")
etiqueta_password.pack()

entrada_password = tk.Entry(ventana, show="*")
entrada_password.pack(pady=5)

# Botón para validar
boton = tk.Button(
	ventana,
	text="Validar credenciales",
	command=capturar_credenciales
)
boton.pack(pady=15)

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack(pady=10)

# Mantener abierta la ventana
ventana.mainloop()
