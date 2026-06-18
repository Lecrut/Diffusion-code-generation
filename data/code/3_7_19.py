"""
Temperature Conversion Module

This module provides highly optimized functions to convert temperatures 
between Celsius (C), Fahrenheit (F), and Kelvin (K).

Conversion Formulas:
- C -> F:    F = C * 9/5 + 32
- F -> C:    C = (F - 32) * 5/9
- K -> C:    C = K - 273.15
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin: float) -> float:
    """Convert temperature from Kelvin to Celsius."""
    return kelvin - 273.15

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    # Sample C to F conversion (0°C should be 32°F)
    c_temp = 0.0
    f_result = celsius_to_fahrenheit(c_temp)
    
    # Sample F to C conversion (212°F should be 100°C)
    f_temp = 212.0
    c_result = fahrenheit_to_celsius(f_temp)
    
    # Sample K to C conversion (373.15K should be 100°C - boiling point of water in Kelvin)
    k_temp = 373.15
    c_k_result = kelvin_to_celsius(k_temp)
    
    print(f"Celsius ({c_temp}) -> Fahrenheit: {f_result}")
    print(f"Fahrenheit ({f_temp}) -> Celsius: {c_result}")
    print(f"Kelvin ({k_temp}) -> Celsius: {c_k_result}")