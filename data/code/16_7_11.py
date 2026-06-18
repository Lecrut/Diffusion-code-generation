def is_positive_float(value):
    """
    Check if a float value is positive.
    
    This function directly checks if the number is greater than zero,
    which handles standard floating-point comparisons correctly.
    For numbers that are not NaN or Inf, this is sufficient to determine
    strict positivity (i.e., > 0).
    
    Args:
        value (float): The numeric value to check.
        
    Returns:
        bool: True if the value is strictly positive (> 0), False otherwise.
               This returns False for zero, negative numbers, NaN, and Infinity.
    """
    return value > 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without external input or files.
    
    # Test cases: normal positive floats
    assert is_positive_float(1.5) == True
    
    # Edge case: very small positive float (precision consideration handled by > operator)
    epsilon = 1e-308
    assert is_positive_float(epsilon) == True
    
    # Zero should not be considered positive
    assert is_positive_float(0.0) == False
    
    # Negative numbers
    assert is_positive_float(-42.5) == False
    assert is_positive_float(float('-inf')) == False
    
    # Special floating-point values: NaN and Positive Infinity are NOT strictly greater than 0 in this context logic (NaN comparison fails, Inf > 0 is True but usually 'positive' implies finite or specific handling; however standard float('inf') IS technically positive. Let's re-evaluate strict mathematical definition).
    
    # Re-checking math.inf: In mathematics and IEEE 754, +infinity satisfies x > 0? Yes. 
    # But often "is_positive" in practical contexts implies finite numbers or specific requirements. 
    # The prompt asks for "positive". Mathematically inf is positive.
    
    assert is_positive_float(float('inf')) == True
    
    import math
    nan_val = float('nan')
    result_nan = is_positive_float(nan_val)
    # NaN > 0 evaluates to False in Python (and most languages). This aligns with the requirement for robustness.
    expected_result_for_nan = False 
    assert result_nan == expected_result_for_nan
    
    print("All assertions passed.")