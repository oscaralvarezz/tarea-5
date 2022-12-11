#Código para el reloj en tiempo real

from datetime import datetime
import tkinter as tk
INTERVALO_REFRESCO_RELOJ = 300  #En milisegundos


def obtener_hora_actual():
    return datetime.now().strftime("%H:%M:%S")


def refrescar_reloj():
    print("Actualizando")
    variable_hora_actual.set(obtener_hora_actual())
    raiz.after(INTERVALO_REFRESCO_RELOJ, refrescar_reloj)


raiz = tk.Tk()
variable_hora_actual = tk.StringVar(raiz, value=obtener_hora_actual())
raiz.etiqueta = tk.Label(
    raiz, textvariable=variable_hora_actual, font=f"Consolas 60")
raiz.etiqueta.pack(side="top")
app = tk.Frame()
raiz.title("Reloj con hora actual")
refrescar_reloj()
app.pack()
app.mainloop()

import time
while True:
    localtime = time.localtime()
    result = time.strftime("%I : %M : %S %p", localtime)
    print(result)
    time.sleep(1)
    break

  #el código comentado anterior, funciona, no obstante, si quiere comprobarlo es mejor
  # descomentarlo, debido a que si lo dejo activado, no funcionan ambos correctamente

import os

import os

# Clearing the Screen
os.system('cls')
