from tkinter import *

# CREATING THE WINDOW

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)


# FUNCTION FOR THE CALCULATE BUTTON
def miles_to_km():
    miles = float(prompt.get())
    km = (miles * 1.609344)
    miles_label.config(text=f"{km:.2f}")


# ENTRY WIDGET
prompt = Entry(width=10)
prompt.grid(column=2, row=1)

# CREATING THE LABELS THAT APPEARS IN OUR PROGRAM
label = Label(window, text="Miles")
label.grid(column=3, row=1)

new_label = Label(window, text="is equal to ")
new_label.grid(column=1, row=2)

miles_label = Label(window, text='0')
miles_label.grid(column=2, row=2)

km_label = Label(window, text="KM")
km_label.grid(column=3, row=2)

# CALCULATE BUTTON
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=4)


window.mainloop()
