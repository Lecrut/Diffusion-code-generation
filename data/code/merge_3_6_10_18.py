"""
Module to calculate the simple weight difference between two given weights.

This module defines a function that computes the absolute difference 
between two numerical values representing weights, handling floating-point 
arithmetic correctly by using standard Python operations which provide sufficient 
precision for typical weight calculations without external libraries like `decimal`.
The result is returned as an integer or float depending on the input types.
"""

def calculate_weight_difference(weight_a: float, weight_b: float) -> float:
    """
    Calculate the simple weight difference between two weights.
    
    This function computes the absolute value of the difference 
    (|weight_a - weight_b|). Floating-point numbers are handled correctly
    using Python's native arithmetic capabilities which maintain precision 
    appropriate for standard numerical computations.

    Args:
        weight_a (float): The first weight value.
        weight_b (float): The second weight value.

    Returns:
        float: The absolute difference between the two weights.
    
    Examples:
        >>> calculate_weight_difference(10.5, 4.2)
        6.3
    
        >>> calculate_weight_difference(-5.0, -8.0)
        3.0
    """
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    # Hard-coded sample values for testing the function without user input or files.
    
    # Sample weights: two different floating-point numbers representing object masses.
    SAMPLE_WEIGHT_A = 157.364 
    SAMPLE_WEIGHT_B = 98.2 
    
    result_difference = calculate_weight_difference(SAMPLE_WEIGHT_A, SAMPLE_WEIGHT_B)
    
    print(f"Weight A: {SAMPLE_WEIGHT_A}")
    print(f"Weight B: {SAMPLE_WEIGHT_B}")
    print(f"Difference: {result_difference}")