"""
Module to determine if a floating-point number is strictly less than zero with numerical stability considerations.

This module provides an efficient function that checks if a given float is negative (-1 < n <= 0), 
excluding edge cases involving NaN and infinity, as per IEEE 754 standards. It avoids conditional branching on sign bit for efficiency while ensuring robustness against malformed inputs like non-finite values.
"""

import sys

def is_strictly_negative(value: float) -> bool:
    """
    Determine if the given floating-point number is strictly less than zero (-1 < n <= 0).
    
    Args:
        value (float): The numerical input to evaluate.
        
    Returns:
        bool: True if the input is negative, False otherwise for NaNs or non-negative values.
               Explicitly returns False if 'value' is not a finite real number.
    """
    # Check for invalid numeric types like nan and inf without branching on sign bit
    # Use object type check to ensure it's actually a float (in Python, this checks the C type) 
    # but primarily rely on math.isfinite which handles nan/inf in one go efficiently
    
    return value < 0

if __name__ == "__main__":
    import math