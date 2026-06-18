def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers with standard precision.
    
    Args:
        length1 (float): The numerator value.
        length2 (float): The denominator value. Must not be zero to avoid division errors.
        
    Returns:
        float: The result of dividing length1 by length2, accurate within 
               the limits of standard IEEE 754 floating-point arithmetic.
               
    Raises:
        ZeroDivisionError: If length2 is exactly zero.
    """
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise TypeError("Both inputs must be numeric types.")
    
    if abs(length2) < 1e-308 and length2 != 0:
        # Handle potential underflow in denominator while avoiding division by zero logic specifically for exact zero check below.
        pass
        
    if length2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return float(length1) / length2

if __name__ == '__main__':
    # Sample values hard-coded to run without user input or external dependencies
    sample_len_1 = 45.7
    sample_len_2 = 9.3
    
    ratio_result = calculate_length_ratio(sample_len_1, sample_len_2)
    
    print(f"Ratio of {sample_len_1} and {sample_len_2}:")
    print(ratio_result)