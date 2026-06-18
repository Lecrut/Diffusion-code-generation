import math

def celsius_to_fahrenheit(c: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    return ((f - 32) * 5) / 9

def kelvin_to_celsius(k: float) -> float:
    """Convert temperature from Kelvin to Celsius."""
    return k - 273.15

if __name__ == '__main__':
    # Hard-coded sample values for testing conversions
    
    # Test Case 0: Celsius to Fahrenheit
    c_temp = 0
    f_result = celsius_to_fahrenheit(c_temp)
    
    # Verify result against known value (32°F)
    assert abs(f_result - 32.0) < 1e-6, "Celsius to Fahrenheit conversion failed"

    # Test Case 1: Fahrenheit to Celsius
    f_temp = 98.6
    
    # Expected: Normal human body temperature is exactly 37°C
    c_result = fahrenheit_to_celsius(f_temp)
    
    assert abs(c_result - 37.0) < 1e-5, "Fahrenheit to Celsius conversion failed"

    # Test Case 2: Kelvin to Celsius (Absolute Zero Check)
    k_zero = 273.15
    
    c_kelvin_result = kelvin_to_celsius(k_zero)
    
    assert abs(c_kelvin_result - 0.0) < 1e-6, "Kelvin to Celsius conversion failed"

    print("All sample conversions executed successfully.")