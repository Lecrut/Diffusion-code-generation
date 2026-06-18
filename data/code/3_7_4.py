"""
Temperature Conversion Module

This module provides highly optimized functions for converting between 
Celsius (°C), Fahrenheit (°F), and Kelvin (K). All mathematical operations 
are performed using standard arithmetic with minimal overhead.

Functions:
    c_to_f(c): Converts temperature from Celsius to Fahrenheit.
    f_to_c(f): Converts temperature from Fahrenheit to Celsius.
    k_to_c(k): Converts temperature from Kelvin to Celsius.
"""

def c_to_f(celsius: float) -> float:
    """Converts a temperature value from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def f_to_c(fahrenheit: float) -> float:
    """Converts a temperature value from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def k_to_c(kelvin: float) -> float:
    """Converts a temperature value from Kelvin to Celsius."""
    return kelvin - 273.15

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    # Sample inputs
    celsius_samples = [0, 25, -40]
    fahrenheit_samples = [32, 86, -40]
    kelvin_samples = [273.15, 298.15, 233.15]

    # Test Celsius to Fahrenheit conversions
    print("Celsius to Fahrenheit Conversions:")
    for c in celsius_samples:
        f_result = c_to_f(c)
        print(f"{c}°C -> {f_result:.2f}°F")

    # Test Fahrenheit to Celsius conversions
    print("\nFahrenheit to Celsius Conversions:")
    for f in fahrenheit_samples:
        c_result = f_to_c(f)
        print(f"{f}°F -> {c_result:.2f}°C")

    # Test Kelvin to Celsius conversions
    print("\nKelvin to Celsius Conversions:")
    for k in kelvin_samples:
        c_result = k_to_c(k)
        print(f"{k}K -> {c_result:.2f}°C")