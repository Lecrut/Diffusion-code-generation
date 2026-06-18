def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers.
    
    Args:
        length1 (float): The numerator value.
        length2 (float): The denominator value. Must not be zero to avoid division by error.
        
    Returns:
        float: The result of dividing length1 by length2, accurate within standard 
              floating-point precision limits.
              
    Raises:
        ZeroDivisionError: If length2 is exactly zero.
    """
    if length2 == 0.0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    return length1 / length2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_length_1 = 15.75
    sample_length_2 = 3.0
    
    ratio_result = calculate_length_ratio(sample_length_1, sample_length_2)
    
    print(f"Ratio of {sample_length_1} to {sample_length_2}: {ratio_result}")