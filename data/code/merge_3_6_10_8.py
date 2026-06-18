"""
Script to calculate the simple weight difference between two given weights.

This module defines a function that computes the absolute difference 
between two floating-point numbers representing weights. It ensures 
correct handling of floating-point precision by using standard arithmetic,
which is appropriate for general scientific and engineering calculations 
where machine epsilon variations are negligible compared to typical measurement scales.

Author: Assistant
Date: 2023-10-27
"""

def calculate_weight_difference(weight_a: float, weight_b: float) -> float:
    """
    Calculate the absolute difference between two weights.

    Args:
        weight_a (float): The first weight value. Can be a positive or negative 
                         floating-point number representing mass magnitude.
        
        weight_b (float): The second weight value. Must match the type of 
                          weight_a for correct arithmetic operation results.

    Returns:
        float: The absolute difference between weight_a and weight_b, ensuring
               a non-negative result by applying abs(). Handles floating-point 
               precision within standard IEEE 754 double-precision limits.

    Raises:
        TypeError: If either input is not an instance of float or int (which acts as float in Python).
    """
    
    # Explicitly validate types to prevent unexpected behavior with non-float inputs
    if not isinstance(weight_a, (int, float)) or not isinstance(weight_b, (int, float)):
        raise TypeError("Both weight parameters must be numeric values.")

    return abs(weight_a - weight_b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    
    # Sample Case 1: Simple positive integers treated as floats
    w_sample_1 = 50.725
    v_sample_1 = 49.83

    result_case_one = calculate_weight_difference(w_sample_1, v_sample_1)
    
    print(f"Difference between {w_sample_1} and {v_sample_1}:")
    print(result_case_one)

    # Sample Case 2: Negative weights (e.g., depth measurements or debt equivalents)
    w_negative = -3.500
    v_negative = -10.275
    
    result_case_two = calculate_weight_difference(w_negative, v_negative)
    
    print(f"Difference between {w_negative} and {v_negative}:")
    print(result_case_two)

    # Sample Case 3: Floating point with high precision digits
    w_high_prec = 100.9999999
    v_high_prec = 274.56
    
    result_case_three = calculate_weight_difference(w_high_prec, v_high_prec)
    
    print(f"Difference between {w_high_prec} and {v_high_prec}:")
    print(result_case_three)

    # Verification of type handling: int passed as float equivalent should work seamlessly in Python.
    w_int_as_float = 50
    result_type_check = calculate_weight_difference(w_int_as_float, v_sample_1)
    
    print(f"Difference between integer {w_int_as_float} and float {v_sample_1}:")
    print(result_type_check)