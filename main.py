from tkinter import*

ventana = Tk()

ventana.geometry("400x400")

label = Label(ventana, text="hola soy un label")
label.pack()

boton = Button(ventana, text="Iniciar")
boton.pack()

ventana.mainloop()
