from tkinter import *

window = Tk()
window.title("Mile To Km Converter")
window.minsize(width=400, height=50)
window.config(padx=20, pady=20)

label_miles = Label(text="Miles", font=("Arial", 16))
label_miles.grid(column=2, row=0)
label_miles.config(padx=10, pady=10)

label_km = Label(text="Km", font=("Arial", 16))
label_km.grid(column=2, row=1)

label_equal = Label(text="is equal to", font=("Arial", 16))
label_equal.grid(column=0, row=1)
label_equal.config(padx=50, pady=1)

label_result_converted = Label(text="0", font=("Arial", 16))
label_result_converted.grid(column=1, row=1)

# Entry
input_miles_entry = Entry(width=7)
input_miles_entry.insert(END, string="0")
input_miles_entry.grid(column=1, row=0)


# Button
def convert():
    miles = float(input_miles_entry.get())
    to_km = round(miles * 1.609)
    label_result_converted.config(text=f"{to_km}")


calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=5, pady=5)


window.mainloop()