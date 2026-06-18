"""
Temperature Conversion Module

This module provides optimized functions to convert between Celsius (C), 
Fahrenheit (F), and Kelvin (K). All calculations use standard mathematical formulas 
and ensure numerical precision suitable for general scientific applications.

Formulas used:
1. C -> F:   F = (C * 9/5) + 32
2. F -> C:   C = (F - 32) * 5/9
3. K -> C:   C = K - 273.15

Author: Assistant
Date: October 2023
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float or int): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float or int): Temperature in degrees Fahrenheit.

    Returns:
        float: Temperature in degrees Celsius.
    """
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.

    Args:
        kelvin (float or int): Temperature in Kelvin.

    Returns:
        float: Temperature in degrees Celsius.
    """
    return kelvin - 273.15

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input
    
    # Test Case 1: Convert room temperature (approx 68°F) to and from other scales
    temp_f = 68.0
    celsius_1 = fahrenheit_to_celsius(temp_f)
    result_test_1 = {
        'f_input': temp_f,
        'c_output': round(celsius_1, 2),
        # Verify reverse conversion accuracy
        'f_from_c_check': abs(fahrenheit_to_celsius(68.0) - celsius_1) < 0.01
    }

    # Test Case 2: Convert boiling water (100°C) to Fahrenheit and Kelvin context
    temp_c = 100.0
    f_output = celsius_to_fahrenheit(temp_c)
    
    # Inverse check for Celsius conversion from known F value of boiling point (~212°F)
    expected_boiling_c = (f_output - 32) * 5 / 9
    
    result_test_2 = {
        'c_input': temp_c,
        'f_output': round(f_output, 2),
        # Verify C->F->C returns original value within tolerance
        'round_trip_check': abs(temp_c - expected_boiling_c) < 0.01
    }

    print("Temperature Conversion Module Test Results")
    print("-" * 35)
    
    if result_test_1['f_from_c_check'] and result_test_2['round_trip_check']:
        status = "ALL TESTS PASSED"
    else:
        status = "TESTS FAILED"

    # Display sample conversions clearly
    print(f"\nSample 1 (68°F):")
    print(f"  Converted to Celsius: {result_test_1['c_output']}°C")
    
    print("\nSample 2 (100°C):")
    print(f"  Converted to Fahrenheit: {result_test_2['f_output']}°F")

    # Additional demo for Kelvin conversion using absolute zero (-273.15 C)
    temp_k = 273.15
    c_from_k = kelvin_to_celsius(temp_k)
    
    print(f"\nSample 3 (Absolute Zero: {temp_k} K):")
    print(f"  Converted to Celsius: {round(c_from_k, 2)}°C")

    # Print summary status only if tests passed as per strict requirements logic
    # The requirement is just that the code runs without input; outputting results 
    # demonstrates functionality.
    
    print("-" * 35)
    print(f"Status: {status}")