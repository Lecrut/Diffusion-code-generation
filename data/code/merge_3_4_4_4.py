"""
Unit Conversion Module: Handles conversions between metric and imperial systems.
This module provides reusable functions to convert length, mass, volume, temperature, 
and speed units without requiring external dependencies or user input.
"""

def meters_to_feet(meters):
    """Converts meters to feet."""
    return meters * 3.28084

def feet_to_meters(feet):
    """Converts feet to meters."""
    return feet / 3.28084

def kilograms_to_pounds(kg):
    """Converts kilograms to pounds."""
    return kg * 2.20462

def pounds_to_kilograms(pounds):
    """Converts pounds to kilograms."""
    return pounds / 2.20462

def liters_to_gallons(liters):
    """Converts liters to US gallons."""
    return liters * 0.264172

def gallons_to_liters(gallons):
    """Converts US gallons to liters."""
    return gallons / 0.264172

def celsius_to_fahrenheit(celsius):
    """Converts Celsius temperature to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5/9

def kilometers_per_hour_to_miles_per_hour(kmh):
    """Converts speed from km/h to mph."""
    return kmh / 1.60934

def miles_per_hour_to_kilometers_per_hour(mph):
    """Converts speed from mph to km/h."""

if __name__ == '__main__':
    # Sample conversions for demonstration purposes
    
    length_samples = {
        "meters": [5, 10.5],
        "feet": [20, 64]
    }

    mass_samples = {
        "kilograms": [7, 30],
        "pounds": [15, 89]
    }

    volume_samples = {
        "liters": [5.5, 12],
        "gallons": [4, 16]
    }

    temp_samples = {
        "celsius": [-40, 37],
        "fahrenheit": [-40, 98.6]
    }

    speed_samples = {
        "kmh": [50, 200],
        "mph": [100, 320]
    }

    print("=== Unit Conversion Module Demo ===\n")

    # Length conversions
    for m in length_samples["meters"]:
        ft = meters_to_feet(m)
        print(f"{m} meters is approximately {ft:.4f} feet.")
    
    for f in length_samples["feet"]:
        mt = feet_to_meters(f)
        print(f"{f} feet is approximately {mt:.4f} meters.\n")

    # Mass conversions
    for k in mass_samples["kilograms"]:
        lb = kilograms_to_pounds(k)
        print(f"{k} kg is approximately {lb:.4f} lbs.")
    
    for p in mass_samples["pounds"]:
        kt = pounds_to_kilograms(p)
        print(f"{p} lbs is approximately {kt:.4f} kg.\n")

    # Volume conversions
    for l in volume_samples["liters"]:
        g = liters_to_gallons(l)
        print(f"{l} L is approximately {g:.4f} US gallons.")
    
    for ga in volume_samples["gallons"]:
        lt = gallons_to_liters(ga)
        print(f"{ga} gal is approximately {lt:.4f} liters.\n")

    # Temperature conversions
    for c in temp_samples["celsius"]:
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C is equal to {f:.2f}°F.")
    
    for fa in temp_samples["fahrenheit"]:
        ce = fahrenheit_to_celsius(fa)
        print(f"{fa}°F is equal to {ce:.2f}°C.\n")

    # Speed conversions
    for k in speed_samples["kmh"]:
        m = kilometers_per_hour_to_miles_per_hour(k)
        print(f"{k} km/h is approximately {m:.4f} mph.")
    
    for mi in speed_samples["mph"]:
        ki = miles_per_hour_to_kilometers_per_hour(mi)
        print(f"{mi} mph is approximately {ki:.4f} km/h.\n")

    print("=== Demo Complete ===")