"""
Module to compare two length measurements and calculate their difference.

This module provides a function that takes two numerical values representing 
lengths, calculates the absolute difference between them, and determines 
which value is greater or if they are equal.

Functions:
    measure_difference(value1, value2) -> tuple[float | int]
        Compares two length measurements and returns their difference and comparison result.

The module contains a main execution block with hard-coded sample values to demonstrate functionality without requiring external input.
"""

def measure_difference(value1: float, value2: float) -> tuple[float, str]:
    """
    Compare two given length measurements.

    Args:
        value1 (float): The first length measurement.
        value2 (float): The second length measurement.

    Returns:
        tuple: A tuple containing the absolute difference between the values 
               and a string indicating the relationship ('greater', 'less', or 'equal').
    
    Example:
        >>> measure_difference(10, 5)
        (5.0, 'value1 is greater than value2')
        >>> measure_difference(3.5, 7.2)
        (3.7, 'value2 is greater than value1')
        >>> measure_difference(4.0, 4.0)
        (0.0, 'values are equal')
    """
    difference = abs(value1 - value2)

    if value1 > value2:
        result_str = "value1 is greater than value2"
    elif value2 > value1:
        result_str = "value2 is greater than value1"
    else:
        result_str = "values are equal"

    return difference, result_str

if __name__ == '__main__':
    # Hard-coded sample values for demonstration. 
    # These run without user input or external dependencies.
    length_a = 250.75
    length_b = 183.9
    
    diff, comparison_result = measure_difference(length_a, length_b)

    print(f"Difference: {diff}")
    print(f"Comparison Result: {comparison_result}")