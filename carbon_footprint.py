# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:50:35 2023

@author: User
"""

import tkinter as tk
from tkinter import simpledialog, messagebox

class CarbonFootprintCalculator:
    def __init__(self):
        self.carbon_factors = {
           'electricity': 0.4,  # kg CO2 per kWh
           'gas': 2.0*30,          # kg CO2 per cubic meter
           'water': 0.02*135,       # kg CO2 per liter
           'waste': 0.3 *0.62        # kg CO2 per kg of waste
        }
        self.total_footprint = 0

    def calculate_electricity_footprint(self, electricity_usage):
        return electricity_usage * self.carbon_factors['electricity']

    def calculate_gas_usage(self, gas_usage):
      gas_usage = 47.5/gas_usage
      return gas_usage * self.carbon_factors['gas']

    def calculate_water_footprint(self, water_usage):
        return water_usage * self.carbon_factors['water']

    def calculate_waste_footprint(self, waste_production):
        return waste_production * self.carbon_factors['waste']

    def calculate_total_footprint(self):
        return self.total_footprint

    def add_to_total_footprint(self, footprint):
        self.total_footprint += footprint


def get_all_user_inputs():
    prompt = "Enter montly home needs:\n(Electricity usage in kWh,how many a gas cylinder last for your family,no of members in family)"
    user_input = simpledialog.askstring("Carbon Footprint Calculator", prompt)
    
    # Split the user input into individual values
    try:
        values = [float(val) for val in user_input.split(',')]
        return values
    except ValueError:
        return None


def display_result(message):
    messagebox.showinfo("Result", message)


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    calculator = CarbonFootprintCalculator()

    # Get all user inputs at once
    user_inputs = get_all_user_inputs()

    if user_inputs is not None and len(user_inputs) == 3:
        # Calculate individual footprints
        electricity_footprint = calculator.calculate_electricity_footprint(user_inputs[0])
        gas_footprint = calculator.calculate_gas_usage(user_inputs[1])
        water_footprint = calculator.calculate_water_footprint(user_inputs[2])
        waste_footprint = calculator.calculate_waste_footprint(user_inputs[2])
        
        # Add individual footprints to the total
        calculator.add_to_total_footprint(electricity_footprint)
        calculator.add_to_total_footprint(gas_footprint)
        calculator.add_to_total_footprint(water_footprint)
        calculator.add_to_total_footprint(waste_footprint)

        # Display total carbon footprint
        total_footprint = calculator.calculate_total_footprint()
        result_message = f"Your total carbon footprint is approximately {total_footprint:.2f} kg CO2 per month."
        display_result(result_message)
       
    else:
        messagebox.showerror("Error", "Invalid input. Please enter values separated by commas.")
        
        


if __name__ == "__main__":
    main()