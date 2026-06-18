"""
Module to calculate simple weight difference between two given weights.

This module defines a function that computes the absolute difference 
between two numeric values, handling both integers and floating-point numbers correctly.
It ensures robustness by using Python's standard arithmetic operations which handle 
decimal precision appropriately for typical use cases without requiring external libraries.

Author: AI Assistant
Date: 2023-10-27
"""

def calculate_weight_difference(weight_a, weight_b):
    """
    Calculates the absolute difference between two weights.

    This function takes two numeric arguments (integers or floats) representing 
    weights and returns their simple arithmetic difference as an absolute value.
    
    Parameters:
        weight_a (float | int): The first weight value.
        weight_b (float | int): The second weight value.

    Returns:
        float: The absolute difference between the two weights.

    Raises:
        TypeError: If either input is not a number or if inputs are non-numeric types.
    
    Examples:
        >>> calculate_weight_difference(10, 5)
        5.0
        >>> calculate_weight_difference(3.5, 2.7)
        0.8
    """
    # Validate input types to ensure only numeric values are processed
    if not isinstance(weight_a, (int, float)) or not isinstance(weight_b, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")

    return abs(weight_a - weight_b)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # These samples cover integer and floating-point scenarios without user interaction.
    
    sample_weight_1 = 250.75
    sample_weight_2 = 300
    
    difference = calculate_weight_difference(sample_weight_1, sample_weight_2)

    print(f"Weight A: {sample_weight_1}")
    print(f"Weight B: {sample_weight_2}")
    print(f"Difference: {difference}")