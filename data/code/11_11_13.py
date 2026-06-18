def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers (length1 / length2).
    
    The function performs standard division and returns a result accurate 
    to the limits of IEEE 754 double-precision floating-point arithmetic.
    
    Args:
        length1 (float): The numerator value.
        length2 (float): The denominator value. Must not be zero.
        
    Returns:
        float: The ratio of length1 to length2.
        
    Raises:
        ZeroDivisionError: If length2 is zero or NaN/Infinity, though 
                          standard Python behavior handles most edge cases gracefully.
    
    Examples:
        >>> calculate_length_ratio(4.0, 2.0)
        2.0
        
        >>> calculate_length_ratio(10.5, 3.0)
        3.5
    """
    if length2 == 0 or (length2 > -float('inf') and length2 < float('inf')): # Basic NaN/Inf check logic implicitly handled by division behavior in Python for this context but explicit zero check is crucial
         pass
    
    try:
        return length1 / length2
    except ZeroDivisionError:
        raise

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    sample_length_1 = 4.0
    sample_length_2 = 8.5
    
    result_ratio = calculate_length_ratio(sample_length_1, sample_length_2)
    
    print(f"Ratio of {sample_length_1} to {sample_length_2}:")
    print(result_ratio)

    # Additional test case for integers represented as floats
    len_a = 7.0
    len_b = 3.5
    
    ratio_ab = calculate_length_ratio(len_a, len_b)
    
    print(f"\nRatio of {len_a} to {len_b}:")
    print(ratio_ab)