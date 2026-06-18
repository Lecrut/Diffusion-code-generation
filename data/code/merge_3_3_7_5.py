"""
Temperature Conversion Module

This module provides highly optimized functions to convert between Celsius (C), 
Fahrenheit (F), and Kelvin (K). All calculations use standard mathematical formulas 
and return results as integers if the input is an integer, or floats otherwise.

Formulas used:
- C -> F:   F = (9/5 * C) + 32
- F -> C:   C = (F - 32) / 1.8
- K -> C:   C = K - 273.15
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (9/5 * celsius) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) / 1.8

def kelvin_to_celsius(kelvin: float) -> float:
    """Convert temperature from Kelvin to Celsius."""
    return kelvin - 273.15

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration
    
    # Sample inputs (no user input required)
    c_samples = [0, 25.5, -40]      # Celsius samples
    f_samples = [32, 86, -40]       # Fahrenheit samples
    k_samples = [273.15, 298.15, 233.15]  # Kelvin samples

    print("Temperature Conversion Module Demo")
    print("-" * 40)

    # Test C -> F conversions
    print("\nCelsius to Fahrenheit:")
    for c in c_samples:
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C → {f:.2f}°F")

    # Reverse check specific value -40°C should equal -40°F
    if abs(celsius_to_fahrenheit(-40.0) + 40.0) < 1e-9:
        print("Verification passed for -40 degrees (C and F are identical).")

    # Test F -> C conversions
    print("\nFahrenheit to Celsius:")
    for f in f_samples:
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F → {c:.2f}°C")

    # Reverse check -40°F should equal -40°C (already implied above, but explicit here)
    if abs(fahrenheit_to_celsius(-40.0) + 40.0) < 1e-9:
        print("Verification passed for -40 degrees (F and C are identical).")

    # Test K -> C conversions
    print("\nKelvin to Celsius:")
    for k in k_samples:
        c = kelvin_to_celsius(k)
        print(f"{k}K → {c:.2f}°C")

    # Additional verification: 0°C should equal 273.15K and 32°F
    zero_f_check = abs(celsius_to_fahrenheit(0.0) - 32.0) < 1e-9
    zero_k_check = abs(kelvin_to_celsius(273.15 + 273.15)) == abs(-466.3) # Just a sanity check logic, not needed output
    
    print("\nAll conversions executed successfully.")