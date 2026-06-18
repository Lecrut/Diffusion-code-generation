"""
Module to calculate the simple weight difference between two given weights.

This module defines a function that computes the absolute difference 
between two numeric values representing weights, ensuring correct handling 
of floating-point numbers by using standard arithmetic operations which 
are precise enough for typical weight calculations unless extreme precision is required.

The script includes a main execution block with hard-coded sample values to demonstrate usage
without requiring any user input or external dependencies.
"""

def calculate_weight_difference(weight_a: float, weight_b: float) -> float:
    """
    Calculate the simple absolute difference between two weights.

    Args:
        weight_a (float): The first weight value.
        weight_b (float): The second weight value.

    Returns:
        float: The absolute difference between weight_a and weight_b.
    
    Example:
        >>> calculate_weight_difference(10.5, 8.2)
        2.3
    """
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No user input, command-line arguments, or network access is used here.
    
    sample_weight_1 = 50.75
    sample_weight_2 = 48.3
    
    difference = calculate_weight_difference(sample_weight_1, sample_weight_2)
    
    print(f"The weight difference between {sample_weight_1} and {sample_weight_2} is: {difference}")