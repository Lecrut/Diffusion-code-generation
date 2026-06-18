"""
Module to determine inequality between two floating-point numbers.

This module provides an optimized method to check if two floats are unequal,
accounting for potential small discrepancies due to floating-point arithmetic.
The standard '!=' operator is generally sufficient and efficient unless specific
tolerance requirements exist; this solution uses the built-in comparison which
is highly optimized in CPython's float implementation.

Author: AI Assistant
Date: 2023
"""

def are_unequal(a, b):
    """
    Determine if two floating-point numbers are unequal.

    This function leverages Python's native equality operator for floats ('!='),
    which is implemented in C and handles the IEEE 754 double-precision logic efficiently.
    It avoids custom epsilon-based comparisons unless a tolerance argument was explicitly requested,
    as '!=' correctly identifies values that are not bit-for-bit identical or mathematically equal 
    within zero tolerance as per standard float semantics.

    Parameters:
        a (float): The first floating-point number.
        b (float): The second floating-point number.

    Returns:
        bool: True if the numbers are unequal, False otherwise.
    
    Example usage without external input is demonstrated in the main block below."""
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    
    test_cases = [
        (1.0, 2.0),           # Clearly unequal
        (3.5, 3.5),           # Identical floats -> Equal
        (float('inf'), float('-inf')), # Significantly different infinities -> Unequal
        (1e-7, -1e-7),        # Opposites -> Unequal
    ]

    for val_a, val_b in test_cases:
        result = are_unequal(val_a, val_b)
        print(f"are_unequal({val_a}, {val_b}) is {result}")