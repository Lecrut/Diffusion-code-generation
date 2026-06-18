"""
Temperature Conversion Module

This module provides highly optimized functions for converting between Celsius (C), 
Fahrenheit (F), and Kelvin (K) temperature scales using standard mathematical formulas.

Formulas:
- C to F: F = C * 9/5 + 32
- F to C: C = (F - 32) * 5/9
- K to C: C = K - 273.15
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    
    Formula: F = C * 1.8 + 32
    """
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in degrees Fahrenheit.

    Returns:
        float: Temperature in degrees Celsius.
    
    Formula: C = (F - 32) * 5/9
    """
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin: float) -> float:
    """
    Convert temperature from Kelvin to Celsius.

    Args:
        kelvin (float): Temperature in Kelvin.

    Returns:
        float: Temperature in degrees Celsius.
    
    Formula: C = K - 273.15
    """
    return kelvin - 273.15

def main():
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample conversions for verification and demonstration
    celsius_samples = [0, 25, -40]
    
    fahrenheit_samples = [32, 86, -40]
    
    kelvin_samples = [273.15, 298.15, 233.15]

    print("Temperature Conversion Results")
    print("-" * 30)

    # Demonstrate Celsius to Fahrenheit conversions using sample values
    print("\nCelsius to Fahrenheit:")
    for c in celsius_samples:
        f = celsius_to_fahrenheit(c)
        print(f"{c:.2f}°C -> {f:.2f}°F")

    # Demonstrate Kelvin to Celsius conversion (since K->C is the only one missing direct input samples, 
    # we convert our Kelvin samples to show the math works correctly for negative C values too)
    
    print("\nKelvin to Celsius:")
    for k in kelvin_samples:
        c = kelvin_to_celsius(k)
        f = celsius_to_fahrenheit(c)  # Double conversion check logic implicitly via chain if needed, 
                                    # but here just showing K->C result
        print(f"{k:.2f}K -> {c:.2f}°C")

    # Show a specific interesting case: -40 degrees where C = F
    special_case_celsius = -40.0
    f_special = celsius_to_fahrenheit(special_case_celsius)
    
    print(f"\nSpecial Case (-40): {special_case_celsius}°C is equal to {f_special:.2f}°F")

    # Show specific Kelvin example: Absolute Zero context (approx 0K would be -273.15 C)
    abs_zero_k = 0.0
    c_abs_zero_kelvin = kelvin_to_celsius(abs_zero_k)
    print(f"Absolute Zero ({abs_zero_k} K): {c_abs_zero_kelvin:.4f}°C")

if __name__ == '__main__':
    main()