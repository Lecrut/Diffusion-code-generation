"""
Module to calculate simple weight difference between two given weights.

This module defines a function that computes the absolute difference 
between two numeric values, ensuring correct handling of floating-point numbers.
It includes a main execution block with hard-coded sample values for testing.

Author: AI Assistant
Date: 2023-10-27
"""

def calculate_weight_difference(weight_a: float, weight_b: float) -> float:
    """
    Calculate the simple absolute difference between two weights.

    This function takes two floating-point numbers representing weights 
    and returns their non-negative difference (absolute value). It uses 
    Python's built-in subtraction to ensure accurate arithmetic operations 
    while respecting standard floating-point precision rules.

    Args:
        weight_a (float): The first weight value.
        weight_b (float): The second weight value.

    Returns:
        float: The absolute difference between the two weights.

    Examples:
        >>> calculate_weight_difference(5.0, 2.3)
        2.7
        
        >>> calculate_weight_difference(-1.5, -4.8)
        3.3
    
    Note:
        Floating-point arithmetic may result in minor precision errors 
        due to binary representation limitations (e.g., 0.1 + 0.2 != 0.3),
        but this function relies on standard Python behavior which is sufficient
        for general weight difference calculations unless arbitrary precision is required.
    """
    return abs(weight_a - weight_b)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample 1: Positive weights with decimal places
    w_sample_1 = 250.75
    v_sample_1 = calculate_weight_difference(w_sample_1, 349.8)
    
    # Sample 2: Negative weights (representing debt or loss in some contexts)
    w_sample_2 = -10.5
    
    # Sample 3: Identical weights resulting in zero difference
    w_identical = 100.0
    
    print(f"Sample 1 Difference ({w_sample_1} vs {v_sample_1}): {abs(w_sample_1 - v_sample_1)}")
    
    print(f"Sample 2 Difference (-{w_sample_2}) and zero: {calculate_weight_difference(-w_sample_2, w_identical):.4f}")