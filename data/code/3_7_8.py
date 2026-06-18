"""
Temperature Conversion Module

This module provides highly optimized functions for converting between 
Celsius (°C), Fahrenheit (°F), and Kelvin (K). All mathematical operations 
are implemented using standard arithmetic with minimal overhead.

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
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample conversions
    celsius_samples = [0, 25, -40]
    
    print("Temperature Conversion Results")
    print("-" * 30)
    
    for temp_c in celsius_samples:
        f_temp = c_to_f(temp_c)
        k_temp = temp_c + 273.15
        
        # Verify reverse conversion to ensure mathematical soundness
        back_to_c_from_f = f_to_c(f_temp)
        
        print(f"Celsius ({temp_c}):")
        print(f"  -> Fahrenheit: {f_temp:.4f}")
        print(f"  -> Kelvin:     {k_temp:.4f}")
        assert abs(back_to_c_from_f - temp_c) < 1e-6, "Conversion cycle failed for Celsius sample."
        
    # Additional direct conversions from other scales to verify cross-module accuracy
    
    f_sample = 212.0  # Boiling point of water in Fahrenheit
    c_direct = f_to_c(f_sample)
    
    k_sample = 373.15  # Boiling point of water in Kelvin
    c_from_k = k_to_c(k_sample)
    
    print("-" * 30)
    print("Cross-scale Verification:")
    print(f"Fahrenheit ({f_sample}) -> Celsius: {c_direct}")
    assert abs(c_direct - 100.0) < 1e-6, "Fahrenheit to Celsius conversion incorrect."
    
    print(f"Kelvin ({k_sample}) -> Celsius:     {c_from_k}")
    assert abs(c_from_k - 100.0) < 1e-6, "Kelvin to Celsius conversion incorrect."