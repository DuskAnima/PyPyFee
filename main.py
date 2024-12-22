import tkinter as tk


def calcular_tarifas_paypal():
    try:
        monto_neto = float(entry_monto_neto.get())
        tipo_transaccion = tipo_transaccion_var.get()

        # Definir tarifas
        tarifa_fija = 0.49  # USD
        if tipo_transaccion == "nacional":
            tarifa_porcentaje = 3.49 / 100
        elif tipo_transaccion == "internacional":
            tarifa_porcentaje = 4.99 / 100
        else:
            raise ValueError("Tipo de transacción inválido.")

        # Calcular monto total
        monto_total = (monto_neto + tarifa_fija) / (1 - tarifa_porcentaje)
        monto_tarifa_porcentaje = monto_total * tarifa_porcentaje
        tarifa_total = monto_tarifa_porcentaje + tarifa_fija

        # Mostrar resultados en el desglose
        label_tarifa_fija.config(text=f"Tarifa fija: ${tarifa_fija:.2f}")
        label_comision.config(text=f"Comisión {tarifa_porcentaje * 100:.2f}%: ${monto_tarifa_porcentaje:.2f}")
        label_monto_neto.config(text=f"Monto neto: ${monto_neto:.2f}")
        label_monto_total.config(text=f"Monto total: ${monto_total:.2f}")

        # Actualizar subtotales
        label_subtotal_tarifa.config(text=f"${tarifa_fija:.2f}")
        label_subtotal_comision.config(text=f"${monto_tarifa_porcentaje + tarifa_fija:.2f}")
        label_subtotal_total.config(text=f"${monto_total:.2f}")

    except ValueError:
        label_resultado.config(text="Por favor, introduce un número válido.", fg="red")


def copiar_monto():
    monto_total = label_monto_total.cget("text").replace("Monto total: $", "")
    ventana.clipboard_clear()
    ventana.clipboard_append(monto_total)
    ventana.update()  # Asegurar que el portapapeles se actualice
    label_resultado.config(text="Monto copiado al portapapeles.", fg="green")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Tarifas PayPal")

# Configurar el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

# Crear elementos de la interfaz
label_instrucciones = tk.Label(ventana, text="Introduce el monto neto recibido (en USD):")
label_instrucciones.grid(row=0, column=0, columnspan=3, pady=10)

entry_monto_neto = tk.Entry(ventana)
entry_monto_neto.grid(row=1, column=0, columnspan=3, pady=5)

# Crear opciones de transacción
tipo_transaccion_var = tk.StringVar(value="internacional")

radio_nacional = tk.Radiobutton(ventana, text="Nacional", variable=tipo_transaccion_var, value="nacional")
radio_nacional.grid(row=2, column=0)

radio_internacional = tk.Radiobutton(ventana, text="Internacional", variable=tipo_transaccion_var, value="internacional")
radio_internacional.grid(row=2, column=1)

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_tarifas_paypal)
boton_calcular.grid(row=2, column=2, pady=10)

# Desglose de tarifas
label_tarifa_fija = tk.Label(ventana, text="Tarifa fija: $0.00", anchor="w")
label_tarifa_fija.grid(row=3, column=0, sticky="w", padx=10)

label_comision = tk.Label(ventana, text="Comisión 4.99%: $0.00", anchor="w")
label_comision.grid(row=4, column=0, sticky="w", padx=10)

label_monto_neto = tk.Label(ventana, text="Monto neto: $0.00", anchor="w")
label_monto_neto.grid(row=5, column=0, sticky="w", padx=10)

# Subtotales
label_subtotal_tarifa = tk.Label(ventana, text="$0.00", anchor="e")
label_subtotal_tarifa.grid(row=3, column=2, sticky="e", padx=10)

label_subtotal_comision = tk.Label(ventana, text="$0.00", anchor="e")
label_subtotal_comision.grid(row=4, column=2, sticky="e", padx=10)

label_subtotal_total = tk.Label(ventana, text="$0.00", anchor="e")
label_subtotal_total.grid(row=5, column=2, sticky="e", padx=10)

# Línea divisoria
frame_divisoria = tk.Frame(ventana, bg="black", height=2, width=400)
frame_divisoria.grid(row=6, column=0, columnspan=3, pady=10)

# Monto total
label_monto_total = tk.Label(ventana, text="Monto total: $0.00", font=("Arial", 12, "bold"))
label_monto_total.grid(row=7, column=0, columnspan=2, pady=10, sticky="w")

boton_copiar = tk.Button(ventana, text="Copiar", command=copiar_monto)
boton_copiar.grid(row=7, column=2, pady=10)

# Mensajes de error o información adicional
label_resultado = tk.Label(ventana, text="", fg="red")
label_resultado.grid(row=8, column=0, columnspan=3, pady=5)

# Iniciar la interfaz gráfica
ventana.mainloop() 
