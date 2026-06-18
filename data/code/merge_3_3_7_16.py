"""
Highly optimized temperature conversion module.

Provides functions to convert between Celsius (C), Fahrenheit (F), 
and Kelvin (K) with mathematical precision suitable for general scientific use.
All calculations avoid unnecessary object creation and complex branching where possible.
"""

def celsius_to_fahrenheit(c: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return c * 1.8 + 32

def fahrenheit_to_celsius(f: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return (f - 32) / 1.8

def kelvin_to_celsius(k: float) -> float:
    """Convert temperature from Kelvin to Celsius."""
    return k - 273.15

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    c_sample = 0.0       # Room temperature in C (approx)
    f_sample = 68.0      # Common indoor temp in F
    k_sample = 273.15   # Freezing point of water in K

    print(f"Celsius to Fahrenheit: {celsius_to_fahrenheit(c_sample)}")
    print(f"Fahrenheit to Celsius: {fahrenheit_to_celsius(f_sample)}")
    print(f"Kelvin to Celsius: {kelvin_to_celsius(k_sample)}")