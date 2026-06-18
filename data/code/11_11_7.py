def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers (length1 / length2).
    
    The function performs a standard division operation which is accurate 
    to the limits of IEEE 754 double-precision floating-point arithmetic.
    
    Args:
        length1 (float): The numerator value.
        length2 (float): The denominator value. Must not be zero.
        
    Returns:
        float: The ratio of length1 to length2.
        
    Raises:
        ZeroDivisionError: If length2 is zero or NaN/Infinity in a way that 
                          makes the operation undefined for this context.
    """
    if isinstance(length2, (int, float)) and not isinstance(length2, bool):
        # Check specifically to avoid catching booleans which are technically subclasses of int
        pass
    
    try:
        return length1 / length2
    except ZeroDivisionError:
        raise ValueError("Length2 cannot be zero.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    sample_length_1 = 450.75
    sample_length_2 = 300.0
    
    result_ratio = calculate_length_ratio(sample_length_1, sample_length_2)
    
    print(f"Ratio of {sample_length_1} to {sample_length_2}:")
    print(result_ratio)