import tkinter as tk
from tkinter import ttk, messagebox

exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.76,
    'JPY': 110.25,
    'INR': 74.56,
    'AUD': 1.34,
    'CAD': 1.25,
    'SGD': 1.36,
    'CHF': 0.92
}

units = {
    'length': {'m': 1.0, 'km': 1000.0, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254},
    'weight': {'kg': 1.0, 'g': 0.001, 'mg': 1e-6, 'lb': 0.453592, 'oz': 0.0283495},
    'volume': {'l': 1.0, 'ml': 0.001, 'm3': 1000.0, 'cm3': 0.001, 'ft3': 28.3168, 'in3': 0.0163871, 'gal': 3.78541, 'qt': 0.946353},
    'time': {'s': 1.0, 'min': 60.0, 'h': 3600.0, 'day': 86400.0, 'week': 604800.0}
}

def convert_currency(from_curren, to_curren, amount):
    if from_curren in exchange_rates and to_curren in exchange_rates:
        conversion_rate = exchange_rates[to_curren] / exchange_rates[from_curren]
        converted_amount = amount * conversion_rate
        return f"{amount} {from_curren} = {converted_amount:.2f} {to_curren}"
    else:
        return 'Invalid currencies. Please enter valid currencies.'

def convert_units(from_unit, to_unit, amount, category):
    if from_unit in units[category] and to_unit in units[category]:
        value_in_base_unit = amount * units[category][from_unit]
        converted_value = value_in_base_unit / units[category][to_unit]
        return f"{amount} {from_unit} = {converted_value:.2f} {to_unit}"
    else:
        return 'Invalid units. Please enter valid units.'

def on_currency_convert():
    try:
        amount = float(currency_amount_entry.get())
        from_curren = from_currency_combobox.get().upper()
        to_curren = to_currency_combobox.get().upper()
        result = convert_currency(from_curren, to_curren, amount)
        currency_result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid numerical value.")

def on_unit_convert():
    try:
        amount = float(unit_amount_entry.get())
        from_unit = from_unit_combobox.get().lower()
        to_unit = to_unit_combobox.get().lower()
        category = unit_category_combobox.get().lower()
        result = convert_units(from_unit, to_unit, amount, category)
        unit_result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid numerical value.")

def update_unit_comboboxes(event):
    category = unit_category_combobox.get().lower()
    from_unit_combobox['values'] = list(units[category].keys())
    to_unit_combobox['values'] = list(units[category].keys())
    from_unit_combobox.set('')
    to_unit_combobox.set('')

def show_currency_converter():
    currency_converter_frame.tkraise()

def show_unit_converter():
    unit_converter_frame.tkraise()

def show_main_menu():
    main_menu_frame.tkraise()

root = tk.Tk()
root.title("Converter")
root.geometry("400x400")

style = ttk.Style(root)
style.theme_use('clam')  
style.configure("TButton", padding=6, relief="flat", background="#D27D2D", foreground="black")
style.configure("TLabel", padding=6, background="#f0f0f0")
style.configure("TFrame", background="#f0f0f0")
style.configure("TCombobox", padding=6, relief="flat")

currency_converter_frame = ttk.Frame(root, padding="20")
unit_converter_frame = ttk.Frame(root, padding="20")

for frame in (currency_converter_frame, unit_converter_frame):
    frame.grid(row=0, column=0, sticky='nsew')

ttk.Label(currency_converter_frame, text="Currency Converter", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(currency_converter_frame, text="From Currency:").grid(row=1, column=0, sticky='e')
from_currency_combobox = ttk.Combobox(currency_converter_frame, values=list(exchange_rates.keys()), state="readonly")
from_currency_combobox.grid(row=1, column=1, pady=5)

ttk.Label(currency_converter_frame, text="To Currency:").grid(row=2, column=0, sticky='e')
to_currency_combobox = ttk.Combobox(currency_converter_frame, values=list(exchange_rates.keys()), state="readonly")
to_currency_combobox.grid(row=2, column=1, pady=5)

ttk.Label(currency_converter_frame, text="Amount:").grid(row=3, column=0, sticky='e')
currency_amount_entry = ttk.Entry(currency_converter_frame)
currency_amount_entry.grid(row=3, column=1, pady=5)

ttk.Button(currency_converter_frame, text="Convert", command=on_currency_convert).grid(row=4, column=0, columnspan=2, pady=10)
currency_result_label = ttk.Label(currency_converter_frame, text="", font=("Helvetica", 12))
currency_result_label.grid(row=5, column=0, columnspan=2)

ttk.Button(currency_converter_frame, text="Back to Main Page", command=show_main_menu).grid(row=6, column=0, columnspan=2, pady=10)

ttk.Label(unit_converter_frame, text="Unit Converter", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(unit_converter_frame, text="Category:").grid(row=1, column=0, sticky='e')
unit_category_combobox = ttk.Combobox(unit_converter_frame, values=list(units.keys()), state="readonly")
unit_category_combobox.grid(row=1, column=1, pady=5)
unit_category_combobox.bind("<<ComboboxSelected>>", update_unit_comboboxes)

ttk.Label(unit_converter_frame, text="From Unit:").grid(row=2, column=0, sticky='e')
from_unit_combobox = ttk.Combobox(unit_converter_frame, state="readonly")
from_unit_combobox.grid(row=2, column=1, pady=5)

ttk.Label(unit_converter_frame, text="To Unit:").grid(row=3, column=0, sticky='e')
to_unit_combobox = ttk.Combobox(unit_converter_frame, state="readonly")
to_unit_combobox.grid(row=3, column=1, pady=5)

ttk.Label(unit_converter_frame, text="Amount:").grid(row=4, column=0, sticky='e')
unit_amount_entry = ttk.Entry(unit_converter_frame)
unit_amount_entry.grid(row=4, column=1, pady=5)

ttk.Button(unit_converter_frame, text="Convert", command=on_unit_convert).grid(row=5, column=0, columnspan=2, pady=10)
unit_result_label = ttk.Label(unit_converter_frame, text="", font=("Helvetica", 12))
unit_result_label.grid(row=6, column=0, columnspan=2)

ttk.Button(unit_converter_frame, text="Back to Main Page", command=show_main_menu).grid(row=7, column=0, columnspan=2, pady=10)

main_menu_frame = ttk.Frame(root, padding="20")
main_menu_frame.grid(row=0, column=0, sticky='nsew')

ttk.Label(main_menu_frame, text="Welcome to the Converter!", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=20)
ttk.Button(main_menu_frame, text="Currency Converter", command=show_currency_converter).grid(row=1, column=0, padx=10, pady=10)
ttk.Button(main_menu_frame, text="Unit Converter", command=show_unit_converter).grid(row=1, column=1, padx=10, pady=10)

main_menu_frame.tkraise()

root.mainloop()