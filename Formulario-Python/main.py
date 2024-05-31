from tkinter import *
from tkinter import ttk

# Lista para almacenar las tarjetas de crédito
tarjetas = []

# Función para abrir la ventana principal
def open_main_window():
    root = Tk()
    root.title("Gestión de Tarjetas de Crédito")
    root.iconbitmap("creditCard.ico")

    # Crear el formulario y el contenedor
    form = ttk.Frame(root, padding=10)
    container = ttk.Frame(root, padding=10)
    form.grid()
    container.grid()

    # Etiqueta y entrada de texto para el número de tarjeta
    ttk.Label(form, text="Ingresar número de tarjeta", font=("Helvetica", 16)).grid(column=0, row=0, pady=10, padx=10)
    numero_entry = ttk.Entry(form, font=("Helvetica", 16))
    numero_entry.grid(column=1, row=0, pady=10, padx=10)

    # Etiqueta y entrada de texto para el nombre del titular
    ttk.Label(form, text="Nombre del titular", font=("Helvetica", 16)).grid(column=0, row=1, pady=10, padx=10)
    nombre_entry = ttk.Entry(form, font=("Helvetica", 16))
    nombre_entry.grid(column=1, row=1, pady=10, padx=10)

    # Etiqueta y entrada de texto para el límite de crédito
    ttk.Label(form, text="Límite de crédito", font=("Helvetica", 16)).grid(column=0, row=2, pady=10, padx=10)
    limite_entry = ttk.Entry(form, font=("Helvetica", 16))
    limite_entry.grid(column=1, row=2, pady=10, padx=10)

    # Botones
    ttk.Button(container, text="Guardar", command=lambda: guardar_tarjeta(numero_entry, nombre_entry, limite_entry)).grid(column=0, row=0, padx=10, pady=10)
    ttk.Button(container, text="Ver Tarjetas", command=lambda: ver_tarjetas(root)).grid(column=1, row=0, padx=10, pady=10)
    ttk.Button(container, text="Salir", command=root.destroy).grid(column=2, row=0, padx=10, pady=10)

    # Crear la barra de menú
    menubar = Menu(root)
    root.config(menu=menubar)

    # Crear el menú 'Archivo'
    archivo_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Archivo", menu=archivo_menu)

    # Agregar opciones al menú 'Archivo'
    archivo_menu.add_command(label="Nuevo", command=lambda: open_new_file(root))
    archivo_menu.add_command(label="Abrir...", command=lambda: print("Abrir Archivo"))
    archivo_menu.add_command(label="Guardar", command=lambda: print("Guardar Archivo"))
    archivo_menu.add_separator()
    archivo_menu.add_command(label="Salir", command=root.quit)

    # Crear el menú 'Editar'
    edit_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Editar", menu=edit_menu)

    # Agregar opciones al menú 'Editar'
    edit_menu.add_command(label="Atras", command=lambda: print("Atras"))
    edit_menu.add_command(label="Adelante", command=lambda: print("Adelante"))
    edit_menu.add_separator()
    edit_menu.add_command(label="Cortar", command=lambda: print("Cortar"))
    edit_menu.add_command(label="Copiar", command=lambda: print("Copiar"))
    edit_menu.add_command(label="Pegar", command=lambda: print("Pegar"))

    # Crear el menú 'Ayuda'
    ayuda_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Ayuda", menu=ayuda_menu)

    # Agregar opciones al menú 'Ayuda'
    ayuda_menu.add_command(label="Acerca de", command=lambda: open_about(root))

# Función para guardar la información de la tarjeta de crédito
def guardar_tarjeta(numero_entry, nombre_entry, limite_entry):
    numero = numero_entry.get()
    nombre = nombre_entry.get()
    limite = limite_entry.get()

    # Validación simple
    if not numero or not nombre or not limite:
        print("Todos los campos son obligatorios")
        return

    try:
        limite = float(limite)
    except ValueError:
        print("El límite de crédito debe ser un número")
        return

    # Guardar la tarjeta de crédito en la lista
    tarjetas.append({"numero": numero, "nombre": nombre, "limite": limite})
    print(f"Tarjeta guardada:\nNúmero: {numero}\nNombre: {nombre}\nLímite: {limite}")

    # Limpiar los campos de entrada
    numero_entry.delete(0, END)
    nombre_entry.delete(0, END)
    limite_entry.delete(0, END)

# Función para ver las tarjetas de crédito en una nueva ventana
def ver_tarjetas(root):
    new_window = Toplevel(root)
    new_window.title("Tarjetas Guardadas")
    new_window.geometry("400x300")

    for tarjeta in tarjetas:
        Label(new_window, text=f"Tarjeta:\nNúmero: {tarjeta['numero']}\nNombre: {tarjeta['nombre']}\nLímite: {tarjeta['limite']}", font=("Helvetica", 12)).pack(pady=5)

    Button(new_window, text="Cerrar", command=new_window.destroy).pack(pady=10)

# Función para abrir la ventana de "Nuevo Archivo"
def open_new_file(root):
    root.withdraw()  # Oculta la ventana principal
    new_window = Toplevel(root)
    new_window.title("Nuevo Archivo")
    new_window.geometry("400x300")

    Label(new_window, text="Esta es una nueva ventana de archivo.", font=("Helvetica", 16)).pack(pady=20)
    Button(new_window, text="Regresar al Inicio", command=lambda: close_window(new_window, root)).pack(pady=10)

# Función para abrir la ventana de "Acerca de"
def open_about(root):
    root.withdraw()  # Oculta la ventana principal
    about_window = Toplevel(root)
    about_window.title("Acerca de")
    about_window.geometry("400x300")

    Label(about_window, text="Esta es la ventana de Acerca de.", font=("Helvetica", 16)).pack(pady=20)
    Button(about_window, text="Regresar al Inicio", command=lambda: close_window(about_window, root)).pack(pady=10)

# Función para cerrar la ventana secundaria y mostrar la principal
def close_window(window, root):
    window.destroy()
    root.deiconify()  # Muestra la ventana principal nuevamente

# Ejecutar la ventana principal al inicio
open_main_window()
mainloop()

