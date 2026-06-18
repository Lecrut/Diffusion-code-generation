"""
Unit Conversion Module: Handles conversions between metric and imperial systems.
This module provides reusable functions to convert length, weight, temperature, 
and volume units without requiring external dependencies or user input.
"""

def meters_to_feet(meters: float) -> float:
    """Convert distance from meters to feet."""
    return meters * 3.28084

def feet_to_meters(feet: float) -> float:
    """Convert distance from feet to meters."""
    return feet / 3.28084

def kilograms_to_pounds(kg: float) -> float:
    """Convert mass from kilograms to pounds."""
    return kg * 2.20462

def pounds_to_kilograms(pounds: float) -> float:
    """Convert mass from pounds to kilograms."""
    return pounds / 2.20462

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def liters_to_gallons(liters: float) -> float:
    """Convert volume from liters to US gallons."""
    return liters / 3.78541

def gallons_to_liters(gallons: float) -> float:
    """Convert volume from US gallons to liters."""
    return gallons * 3.78541

if __name__ == '__main__':
    # Sample conversions for demonstration purposes
    
    length_samples = [10, 20]  # meters
    weight_samples = [5, 10]   # kilograms
    temp_samples = [0, 100]    # Celsius
    vol_samples = [18.9, 37.8541]  # liters

    print("=== Unit Conversion Results ===\n")

    for m in length_samples:
        ft = meters_to_feet(m)
        print(f"{m} meter(s) is equal to {ft:.2f} foot(s)")

    for kg in weight_samples:
        lbs = kilograms_to_pounds(kg)
        print(f"{kg} kilogram(me) is equal to {lbs:.2f} pound(s)")

    for c in temp_samples:
        f = celsius_to_fahrenheit(c)
        print(f"{c} degree Celsius is equal to {f:.2f} degrees Fahrenheit")

    for l in vol_samples:
        gal = liters_to_gallons(l)
        print(f"{l} liter(s) is equal to {gal:.4f} US gallon(s)")