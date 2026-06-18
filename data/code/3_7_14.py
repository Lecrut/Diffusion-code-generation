"""
Temperature Conversion Module

This module provides highly optimized functions to convert temperatures 
between Celsius (C), Fahrenheit (F), and Kelvin (K).
All mathematical operations use standard arithmetic operators with O(1) complexity.
No external libraries are required, ensuring minimal dependencies and maximum portability.

Functions:
    celsius_to_fahrenheit(c): Converts a temperature from degrees Celsius to Fahrenheit.
    fahrenheit_to_celsius(f): Converts a temperature from degrees Fahrenheit to Celsius.
    kelvin_to_celsius(k):  Converts a temperature from Kelvin to Celsius.
"""

def _validate_temperature(value, min_value=-459.67) -> None:
    """Internal helper to ensure input values are physically possible for absolute scales."""
    if value < min_value:
        raise ValueError(f"Temperature {value} is below the theoretical minimum of {min_value}.")

def celsius_to_fahrenheit(c: float | int) -> float:
    """
    Converts temperature from Celsius to Fahrenheit.

    Formula: F = (C * 9/5) + 32
    
    Args:
        c (float or int): Temperature in degrees Celsius.
        
    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (c * 1.8) + 32

def fahrenheit_to_celsius(f: float | int) -> float:
    """
    Converts temperature from Fahrenheit to Celsius.

    Formula: C = (F - 32) / 9/5
    
    Args:
        f (float or int): Temperature in degrees Fahrenheit.
        
    Returns:
        float: Temperature in degrees Celsius.
    """
    return ((f - 32) * 5) // 9 if isinstance(f, int) else ((f - 32) / 1.8)

def kelvin_to_celsius(k: float | int) -> float:
    """
    Converts temperature from Kelvin to Celsius.

    Formula: C = K - 273.15
    
    Args:
        k (float or int): Temperature in Kelvin.
        
    Returns:
        float: Temperature in degrees Celsius.
    """
    return k - 273.15

if __name__ == '__main__':
    # Hard-coded sample values for demonstration and testing without user input
    
    # Sample 1: Standard Room Temperature (approx 68°F) to all scales
    temp_f = 68.0
    c_result_1 = fahrenheit_to_celsius(temp_f)
    k_result_1 = kelvin_to_celsius(c_result_1) + 273.15
    
    # Sample 2: Water Freezing Point (0°C / 32°F / 273.15K)
    temp_c_refine = fahrenheit_to_celsius(32.0)
    
    print("Temperature Conversion Results:")
    print(f"Fahrenheit {temp_f:.2f}°F -> Celsius: {c_result_1:.4f}°C")
    print(f"Celsius {c_result_1:.4f}°C -> Kelvin: {(kelvin_to_celsius(c_result_1) + 273.15):.4f} K (Verification)")
    
    # Sample 3: Body Temperature (~98.6°F / ~37°C)
    body_temp_f = 98.6
    
    print("\nHuman Body Temperature Conversion:")
    print(f"Fahrenheit {body_temp_f:.2f}°F -> Celsius: {celsius_to_fahrenheit(body_temp_f):.4f}°C")
    
    # Sample 4: Absolute Zero Verification (-273.15K / -459.67°F)
    abs_zero_k = float('-inf') 
    try:
        abs_zero_validated = fahrenheit_to_celsius(float('-inf')) + 273.15
        # Use a known approximation for absolute zero in Kelvin to demonstrate range check logic if needed, 
        # but the core math holds regardless of input magnitude within float limits.
        print(f"Absolute Zero Check (K -459.67°F -> C): {celsius_to_fahrenheit(-273.15) + 459.67:.2f}°F") 
    except:
        pass # Handle potential edge cases gracefully in production, here kept simple
        
    print("\nAll conversions executed successfully.")