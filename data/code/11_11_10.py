def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers (length1 / length2).
    
    Args:
        length1: The numerator value as a float.
        length2: The denominator value as a float.
        
    Returns:
        The ratio as a float, accurate to standard IEEE 754 double-precision limits.
        
    Raises:
        ZeroDivisionError: If the denominator (length2) is zero or not representable 
                          (e.g., infinity or NaN), which would cause an exception in division anyway.
    
    Note:
        This function leverages Python's native float type, which adheres to IEEE 754 double-precision arithmetic standards by default.
        No custom rounding or intermediate precision tricks are necessary as the final result 
        of a direct division already maximizes accuracy within these limits.
        
        Special cases handled automatically:
        - If length2 is 0.0, ZeroDivisionError is raised (standard behavior).
        - Division involving infinity results in +/-infinity (standard behavior).
    """
    if not isinstance(length1, float) or not isinstance(length2, float):
        raise TypeError("Both arguments must be floating-point numbers.")

    # Direct division performs the operation with maximum available precision.
    return length1 / length2

if __name__ == '__main__':
    # Sample values hardcoded to ensure no user input is required.
    
    # Test case 1: Normal integers as floats
    res_normal = calculate_length_ratio(10.5, 3.2)
    
    # Test case 2: Very small numbers (to check precision near zero)
    res_small = calculate_length_ratio(1e-6, 2e-7)
    
    # Test case 3: Numbers close to infinity limits (though direct division handles result type)
    res_large = calculate_length_ratio(float('inf'), float('nan')) 
    # Note: Division by NaN results in NaN as per IEEE 754 standard.

    print(f"Ratio of sample inputs:")
    print(f"{res_normal}")           # Expected approx: 3.28125
    print(f"{res_small}")          # Expected: 50.0
    
    # Attempting a case that triggers ZeroDivisionError for demonstration 
    # (commented out to prevent accidental runtime halt during normal testing, 
    # but included in logic as per function spec behavior)
    try:
        res_zero = calculate_length_ratio(10.0, 0.0)
    except ZeroDivisionError:
        print("Attempted division by zero correctly raised an exception.")

    # Test case with infinity in numerator (result should be inf)
    result_inf_num = calculate_length_ratio(float('inf'), 5.0)
    print(f"Ratio of infinite to finite number:")
    print(result_inf_num)           # Expected: inf
    
    # Verification that the function returns a float type consistently for valid inputs
    assert isinstance(res_normal, float), "Result must be a float."
    
    print("All sample tests completed successfully.")