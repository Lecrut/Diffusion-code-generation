"""
Module to calculate simple weight difference between two given weights.

This module defines a function that computes the absolute difference 
between two numerical values representing weights, ensuring correct handling 
of floating-point numbers by using standard arithmetic operations which are 
precise enough for typical weight calculations in this context.

The implementation avoids external dependencies and interactive input methods,
relying solely on built-in Python types (float/int) and basic operators.
"""

def calculate_weight_difference(weight_a: float, weight_b: float) -> float:
    """
    Calculate the simple absolute difference between two weights.

    This function takes two numeric values representing weights and returns 
    their non-negative difference. It handles both integer and floating-point 
    inputs correctly by promoting them to floats before subtraction if necessary.

    Args:
        weight_a (float): The first weight value.
        weight_b (float): The second weight value.

    Returns:
        float: The absolute difference between the two weights.

    Example:
        >>> calculate_weight_difference(10.5, 4.2)
        6.3
        >>> calculate_weight_difference(-3.7, -8.9)
        5.2
    """
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    SAMPLE_WEIGHT_A = 10.5
    SAMPLE_WEIGHT_B = 4.2

    result = calculate_weight_difference(SAMPLE_WEIGHT_A, SAMPLE_WEIGHT_B)
    
    print(f"Weight A: {SAMPLE_WEIGHT_A}")
    print(f"Weight B: {SAMPLE_WEIGHT_B}")
    print(f"Difference: {result}")