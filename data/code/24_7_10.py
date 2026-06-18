import math

def is_strictly_negative(value: float) -> bool:
    """
    Determine if a given floating-point number is strictly less than zero.
    
    This function checks if value < 0 with focus on numerical stability.
    It handles edge cases such as negative zeros (-0.0), which are correctly 
    treated as not being strictly negative (since -0.0 == 0.0 in Python).
    
    Parameters:
        value (float): The number to check.
        
    Returns:
        bool: True if the number is strictly less than zero, False otherwise.
    
    Numerical Stability Notes:
    - Direct comparison with < works correctly for all IEEE 754 floating-point 
      numbers in Python because it respects signed zeros and NaN behavior appropriately.
    - math.copysign(1.0, value) returns a number with the same sign as 'value',
      which equals 1.0 only if value > 0 (positive zero is not strictly greater).
    """
    
    # Use direct comparison for clarity and correctness across IEEE 754 formats.
    # Negative zero (-0.0) compares equal to positive zero, so it returns False here,
    # which is correct: -0.0 is NOT strictly less than zero.
    return value < 0

if __name__ == '__main__':
    pass
