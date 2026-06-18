"""
Unit Conversion Module: Handles conversions between metric (SI) and imperial systems.
This module provides reusable functions to convert length, mass, volume, temperature, 
and speed units without requiring user input or external dependencies.
"""

def meters_to_feet(meters):
    """Converts distance from meters to feet."""
    return meters * 3.28084

def feet_to_meters(feet):
    """Converts distance from feet to meters."""
    return feet / 3.28084

def kilograms_to_pounds(kg):
    """Converts mass from kilograms to pounds."""
    return kg * 2.20462

def pounds_to_kilograms(pounds):
    """Converts mass from pounds to kilograms."""
    return pounds / 2.20462

def liters_to_gallons(liters):
    """Converts volume from liters (US) to gallons (US)."""
    return liters * 0.264172

def gallons_to_liters(gallons):
    """Converts volume from US gallons to liters."""
    return gallons / 0.264172

def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def kilometers_per_hour_to_miles_per_hour(kmph):
    """Converts speed from kilometers per hour to miles per hour."""
    return kmph / 1.60934

def mph_to_kilometers_per_hour(mph):
    """Converts speed from miles per hour to kilometers per hour."""
    return mph * 1.60934

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes
    
    print("Unit Conversion Demonstration")
    
    length_samples = [5, 20]
    mass_samples = [7.5, 150]
    volume_samples = [3.8, 40]
    temp_samples = [-4, 98.6]
    speed_samples = [100, 60]

    print("\n--- Length Conversion ---")
    for m in length_samples:
        ft = meters_to_feet(m)
        print(f"{m} meters is approximately {ft:.2f} feet.")
    
    for f in length_samples[::-1]: # Reverse list to show reverse conversion with same values roughly
        pass 
    # Re-calculate specific foot value from the first sample for clarity if needed, but general loop works.
    # Let's just demonstrate one-way and then swap inputs conceptually by reusing logic on different numbers or swapping roles.
    
    print("\n--- Mass Conversion ---")
    for kg in mass_samples:
        lbs = kilograms_to_pounds(kg)
        print(f"{kg} kg is approximately {lbs:.2f} lb.")

    print("\n--- Volume Conversion (US Gallons) ---")
    for l in volume_samples:
        gal = liters_to_gallons(l)
        print(f"{l} L is approximately {gal:.4f} US gallons.")

    print("\n--- Temperature Conversion ---")
    for c in temp_samples:
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C is equivalent to {f:.2f}°F.")

    print("\n--- Speed Conversion (km/h -> mph) ---")
    for kph in speed_samples:
        mph_val = kilometers_per_hour_to_miles_per_hour(kph)
        print(f"{kph} km/h is approximately {mph_val:.4f} mph.")
    
    # Demonstrate reverse conversions with specific values to show reusability
    
    sample_kg = 10.5
    sample_ft = 65
    sample_celsius = 25

    print(f"\n--- Reusable Reverse Conversions ---")
    lbs_val = pounds_to_kilograms(sample_kg * 2) # Double the original to make it a nice round number for reverse check logic if desired, or just convert back. 
    # Actually let's just show converting specific values directly without intermediate steps in main block
    
    print(f"Converting {sample_celsius}°C -> °F: {celsius_to_fahrenheit(sample_celsius):.2f}")
    
    meters_from_ft = feet_to_meters(10)
    ft_back = meters_to_feet(meters_from_ft)
    diff = abs(ft - ft_back) < 0.001 # Check if conversion is reversible within precision
    
    print(f"Converting {meters_from_ft:.4f} m -> ft: {ft_back:.2f} (Original was 10 ft)")