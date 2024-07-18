import tkinter as tk
from tkinter import ttk
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Charger le modèle prédictif
model = pickle.load(open('model.pkl', 'rb'))

# Fonction de prédiction adaptée pour Tkinter
def predict_price():
    Fuel_Type_Diesel = 0
    Present_Price = float(entry_present_price.get())
    Kms_Driven = int(entry_kms_driven.get())
    Kms_Driven2 = np.log(Kms_Driven)  # Example transformation, check if appropriate
    Owner = int(entry_owner.get())
    
    Fuel_Type_n = combobox_fuel_type.current()  # Assuming Fuel_Type_n is an index in combobox
    if Fuel_Type_n == 0:  # Assuming index 0 corresponds to Diesel
        Fuel_Type_Diesel = 1
    else:
        Fuel_Type_Diesel = 0
    
    Transmission_n = combobox_transmission.current()  # Assuming Transmission_n is an index in combobox
    if Transmission_n == 0:  # Assuming index 0 corresponds to Manual
        Transmission_Mannual = 1
    else:
        Transmission_Mannual = 0
    
    Year = int(entry_year.get())
    Year = 2020 - Year  # Adjusting year as needed
    
    # Adjust the features based on your model's expectations
    prediction = model.predict([[Year, Present_Price, Kms_Driven, Fuel_Type_n, Transmission_n]])
    output = round(prediction[0], 2)
    
    if output < 0:
        result_label.config(text="Sorry you cannot sell this car")
    else:
        result_label.config(text="You Can Sell The Car at {}".format(output))

# Créer une fenêtre Tkinter
root = tk.Tk()
root.title("Car Price Prediction")

# Widgets
label_present_price = ttk.Label(root, text="Enter Present Price:")
label_present_price.grid(row=0, column=0, padx=10, pady=10)
entry_present_price = ttk.Entry(root, width=15)
entry_present_price.grid(row=0, column=1, padx=10, pady=10)

label_kms_driven = ttk.Label(root, text="Enter Kms Driven:")
label_kms_driven.grid(row=1, column=0, padx=10, pady=10)
entry_kms_driven = ttk.Entry(root, width=15)
entry_kms_driven.grid(row=1, column=1, padx=10, pady=10)

label_owner = ttk.Label(root, text="Enter Owner:")
label_owner.grid(row=2, column=0, padx=10, pady=10)
entry_owner = ttk.Entry(root, width=15)
entry_owner.grid(row=2, column=1, padx=10, pady=10)

label_fuel_type = ttk.Label(root, text="Select Fuel Type:")
label_fuel_type.grid(row=3, column=0, padx=10, pady=10)
fuel_types = ['Petrol', 'Diesel']
combobox_fuel_type = ttk.Combobox(root, values=fuel_types, width=12)
combobox_fuel_type.grid(row=3, column=1, padx=10, pady=10)

label_year = ttk.Label(root, text="Enter Year:")
label_year.grid(row=4, column=0, padx=10, pady=10)
entry_year = ttk.Entry(root, width=15)
entry_year.grid(row=4, column=1, padx=10, pady=10)

label_seller_type = ttk.Label(root, text="Select Seller Type:")
label_seller_type.grid(row=5, column=0, padx=10, pady=10)
seller_types = ['Individual', 'Dealer']
combobox_seller_type = ttk.Combobox(root, values=seller_types, width=12)
combobox_seller_type.grid(row=5, column=1, padx=10, pady=10)

label_transmission = ttk.Label(root, text="Select Transmission:")
label_transmission.grid(row=6, column=0, padx=10, pady=10)
transmission_types = ['Mannual', 'Automatic']
combobox_transmission = ttk.Combobox(root, values=transmission_types, width=12)
combobox_transmission.grid(row=6, column=1, padx=10, pady=10)

predict_button = ttk.Button(root, text="Predict Price", command=predict_price)
predict_button.grid(row=7, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=8, columnspan=2, padx=10, pady=10)

# Boucle principale Tkinter
root.mainloop()
