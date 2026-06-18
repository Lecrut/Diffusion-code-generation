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
    
    # Sample conversions
    celsius_samples = [0, 25, -40]
    
    print("Temperature Conversion Results")
    print("-" * 30)
    
    for temp_c in celsius_samples:
        f_temp = c_to_f(temp_c)
        k_temp = temp_c + 273.15
        
        # Verify reverse conversion accuracy within floating point tolerance
        assert abs(f_to_c(f_temp) - temp_c) < 0.0001, "Fahrenheit to Celsius round-trip failed"
        
        print(f"{temp_c}°C = {f_temp:.2f}°F")
        print(f"{temp_c}°C = {k_temp:.2f}K\n")

    # Additional direct conversions for demonstration
    sample_f = 68.0
    result_fc = f_to_c(sample_f)
    
    sample_k = 373.15
    result_ka = k_to_c(sample_k)
    
    print(f"Direct Verification:")
    print(f"{sample_f}°F -> {result_fc:.2f}°C")
    print(f"{sample_k}K -> {result_ka:.2f}°C")