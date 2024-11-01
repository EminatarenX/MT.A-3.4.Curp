import tkinter as tk
from tkinter import ttk

# Lista de estados de México
estados_mexico = (
    "AGUASCALIENTES", "BAJA CALIFORNIA", "BAJA CALIFORNIA SUR", "CAMPECHE", "CHIAPAS", 
    "CHIHUAHUA", "CIUDAD DE MÉXICO", "COAHUILA", "COLIMA", "DURANGO", 
    "GUANAJUATO", "GUERRERO", "HIDALGO", "JALISCO", "MÉXICO", 
    "MICHOACÁN", "MORELOS", "NAYARIT", "NUEVO LEÓN", "OAXACA", 
    "PUEBLA", "QUERÉTARO", "QUINTANA ROO", "SAN LUIS POTOSÍ", "SINALOA", 
    "SONORA", "TABASCO", "TAMAULIPAS", "TLAXCALA", "VERACRUZ", 
    "YUCATÁN", "ZACATECAS"
)

def generar_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado):
    nombre = nombre.strip().upper()
    apellido_paterno = apellido_paterno.strip().upper()
    apellido_materno = apellido_materno.strip().upper()
    fecha_nacimiento = fecha_nacimiento.strip()
    sexo = sexo.strip().upper()
    estado = estado.strip().upper()

    # Obtener primera letra y primera vocal interna del apellido paterno
    primera_letra_paterno = apellido_paterno[0]
    primera_vocal_paterno = next((c for c in apellido_paterno[1:] if c in 'AEIOU'), 'X')

    # Obtener primera letra del apellido materno y del nombre
    primera_letra_materno = apellido_materno[0] if apellido_materno else 'X'
    primera_letra_nombre = nombre[0]

    # Extraer año, mes y día de la fecha de nacimiento
    año, mes, dia = fecha_nacimiento[:4], fecha_nacimiento[5:7], fecha_nacimiento[8:]

    # Formar CURP básica
    curp = (primera_letra_paterno + primera_vocal_paterno + primera_letra_materno + primera_letra_nombre +
            año[2:] + mes + dia + sexo + estado[:2])

    # Añadir homoclave (ejemplo simple, en la realidad se genera más compleja)
    homoclave = "01"
    curp += homoclave

    return curp

def run_turing_machine(input_nombre, input_apellido_paterno, input_apellido_materno, input_fecha_nacimiento, input_sexo, input_estado):
    nombre = input_nombre.get()
    apellido_paterno = input_apellido_paterno.get()
    apellido_materno = input_apellido_materno.get()
    fecha_nacimiento = input_fecha_nacimiento.get()
    sexo = input_sexo.get()
    estado = input_estado.get()

    curp = generar_curp(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, estado)

    results_table.insert("", tk.END, values=(nombre, apellido_paterno + ' ' + apellido_materno, 
                                             fecha_nacimiento, estado, sexo, curp))
    return True

root = tk.Tk()
root.geometry("1280x720")
root.title("Generador de CURP")

# Etiquetas y campos de entrada para cada dato
input_label = tk.Label(root, text="Nombre")
input_label.pack()
input_field_nombre = tk.Entry(root)
input_field_nombre.pack()

input_label_apellido_paterno = tk.Label(root, text="Apellido Paterno")
input_label_apellido_paterno.pack()
input_field_apellido_paterno = tk.Entry(root)
input_field_apellido_paterno.pack()

input_label_apellido_materno = tk.Label(root, text="Apellido Materno")
input_label_apellido_materno.pack()
input_field_apellido_materno = tk.Entry(root)
input_field_apellido_materno.pack()

input_label_fecha_nacimiento = tk.Label(root, text="Fecha de Nacimiento (AAAA-MM-DD)")
input_label_fecha_nacimiento.pack()
input_field_fecha_nacimiento = tk.Entry(root)
input_field_fecha_nacimiento.pack()

# Campo para el sexo (usando Combobox)
input_label_sexo = tk.Label(root, text="Sexo")
input_label_sexo.pack()
input_field_sexo = ttk.Combobox(root, values=["H", "M"])
input_field_sexo.pack()

# Campo para el estado (usando Combobox)
input_label_estado = tk.Label(root, text="Estado de Nacimiento")
input_label_estado.pack()
input_field_estado = ttk.Combobox(root, values=estados_mexico)
input_field_estado.pack()

# Botón de validación y tabla de resultados
run_button = tk.Button(root, text="Generar CURP", command=lambda: run_turing_machine(
    input_field_nombre, input_field_apellido_paterno, input_field_apellido_materno, 
    input_field_fecha_nacimiento, input_field_sexo, input_field_estado
))
run_button.pack()

results_table = ttk.Treeview(root, columns=("Nombre", "Apellidos", "Fecha de nacimiento", "Entidad Federativa", "Sexo", "CURP"), show="headings")
results_table.heading("Nombre", text="Nombre")
results_table.heading("Apellidos", text="Apellidos")
results_table.heading("Fecha de nacimiento", text="Fecha de nacimiento")
results_table.heading("Entidad Federativa", text="Entidad Federativa")
results_table.heading("Sexo", text="Sexo")
results_table.heading("CURP", text="CURP")
results_table.pack()

result_label = tk.Label(root, text="", fg="red")
result_label.pack()

root.mainloop()
