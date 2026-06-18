import math

def celsius_to_fahrenheit(c: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9

def kelvin_to_celsius(k: float) -> float:
    """Convert temperature from Kelvin to Celsius."""
    return k - 273.15

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration
    
    # Sample conversions
    c_temp = 0.0      # Freezing point of water in Celsius
    f_result = celsius_to_fahrenheit(c_temp)
    
    h_temp = -459.67 # Absolute zero in Fahrenheit (approximated to standard float precision context usually, but exact is defined by absolute zero physics constant relationship actually 273.15K * 9/5 + 32? No. Abs Zero F = -459.67)
    c_from_f = fahrenheit_to_celsius(h_temp)
    
    k_abs_zero = 0.0 # Absolute zero in Kelvin
    
    print(f"Celsius to Fahrenheit: {c:.1f} °C -> {f:.2f} °F")
    print("Note on the sample above, C=0 is freezing water.")