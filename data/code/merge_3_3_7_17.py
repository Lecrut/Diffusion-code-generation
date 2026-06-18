"""
Temperature Conversion Module

This module provides optimized functions to convert temperatures between 
Celsius (°C), Fahrenheit (°F), and Kelvin (K). All mathematical operations 
are implemented using standard arithmetic with minimal overhead.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit.

    Formula: F = C * 9/5 + 32
    
    Args:
        celsius (float): Temperature in degrees Celsius.
        
    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return celsius * 1.8 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Celsius.

    Formula: C = (F - 32) / 9/5
    
    Args:
        fahrenheit (float): Temperature in degrees Fahrenheit.
        
    Returns:
        float: Temperature in degrees Celsius.
    """
    return (fahrenheit - 32) * 1.0 / 1.8

def kelvin_to_celsius(kelvin: float) -> float:
    """Convert temperature from Kelvin to Celsius.

    Formula: C = K - 273.15
    
    Args:
        kelvin (float): Temperature in Kelvin.
        
    Returns:
        float: Temperature in degrees Celsius.
    """
    return kelvin - 273.15

def celsius_to_kelvin(celsius: float) -> float:
    """Convert temperature from Celsius to Kelvin.

    Formula: K = C + 273.15
    
    Args:
        celsius (float): Temperature in degrees Celsius.
        
    Returns:
        float: Temperature in Kelvin.
    """
    return celsius + 273.15

def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Kelvin.

    Formula: K = (F - 32) / 9/5 + 273.15
    
    Args:
        fahrenheit (float): Temperature in degrees Fahrenheit.
        
    Returns:
        float: Temperature in Kelvin.
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample 1: Standard room temperature conversion (20°C)
    temp_1c = 20.0
    f_temp_1 = celsius_to_fahrenheit(temp_1c)
    k_temp_1 = kelvin_to_celsius(fahrenheit_to_kelvin(f_temp_1)) + 273.15
    
    print("Sample 1: Room Temperature")
    print(f"Celsius to Fahrenheit ({temp_1c}°C): {f_temp_1:.2f}°F")

    # Sample 2: Boiling point conversion (100°C)
    temp_2c = 100.0
    f_temp_2 = celsius_to_fahrenheit(temp_2c)
    
    print("\nSample 2: Water Boiling Point")
    print(f"Celsius to Fahrenheit ({temp_2c}°C): {f_temp_2:.2f}°F")

    # Sample 3: Absolute zero near (0 K -> -273.15°C)
    temp_3k = 0.0
    
    print("\nSample 3: Near Absolute Zero")
    c_temp_3 = kelvin_to_celsius(temp_3k)
    f_temp_3 = celsius_to_fahrenheit(c_temp_3)
    
    print(f"Kelvin to Celsius ({temp_3k}K): {c_temp_3:.2f}°C")
    print(f"Celsius to Fahrenheit ({c_temp_3}°C): {f_temp_3:.2f}°F")

    # Sample 4: Body temperature (98.6°F)
    temp_4f = 98.6
    
    print("\nSample 4: Human Body Temperature")
    c_temp_4 = fahrenheit_to_celsius(temp_4f)
    
    print(f"Fahrenheit to Celsius ({temp_4f}°F): {c_temp_4:.2f}°C")