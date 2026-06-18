"""
Module to compare two length measurements.

This module defines a function that takes two numeric values representing lengths,
calculates their difference (first minus second), and determines which value is greater,
less than, or equal to the other. The comparison handles both positive and negative numbers,
treating them as signed magnitudes where applicable for direct subtraction logic.

Functions:
    compare_lengths(value1, value2) -> tuple[float, str]
        Compares two length values and returns their difference and a status string.

Usage Example:
    >>> diff, result = compare_lengths(50, 30)
    >>> print(f"Difference: {diff}, Result: {result}")
    Difference: 20.0, Result: greater than
"""

def compare_lengths(value1: float | int, value2: float | int) -> tuple[float, str]:
    """
    Compare two length measurements and return their difference and comparison result.

    Args:
        value1 (float or int): The first length measurement.
        value2 (float or int): The second length measurement.

    Returns:
        tuple[float, str]: A tuple containing the numeric difference (value1 - value2)
                           and a string indicating whether value1 is greater than, less than, 
                           or equal to value2.

    Examples:
        compare_lengths(50, 30) returns (20.0, 'greater than')
        compare_lengths(30, 50) returns (-20.0, 'less than')
        compare_lengths(10, 10) returns (0.0, 'equal to')
    """
    difference = value1 - value2
    
    if difference > 0:
        result_str = "greater than"
    elif difference < 0:
        result_str = "less than"
    else:
        result_str = "equal to"
        
    return float(difference), result_str

if __name__ == '__main__':
    # Hard-coded sample values for testing the compare_lengths function.
    # No user input, command-line arguments, or external dependencies are used.
    
    measurement_a: int = 105
    measurement_b: int = 87
    
    diff_val, comp_result = compare_lengths(measurement_a, measurement_b)
    
    print(f"Comparing {measurement_a} and {measurement_b}")
    print(f"Difference: {diff_val}")
    print(f"Result: {comp_result}")