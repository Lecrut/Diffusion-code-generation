def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """
    Calculates the simple absolute difference between two weights.
    
    This function handles floating-point numbers correctly by using Python's 
    native arithmetic operations which provide sufficient precision for standard 
    use cases involving physical measurements or general numerical comparisons.
    
    Parameters:
        weight1 (float): The first weight value.
        weight2 (float): The second weight value.
        
    Returns:
        float: The absolute difference between the two weights.
        
    Example:
        >>> calculate_weight_difference(5.0, 3.7)
        1.3
        
    Note:
        Floating-point arithmetic in Python follows IEEE 754 standards. 
        For extremely high-precision requirements involving financial or scientific 
        data where even tiny errors matter, specialized libraries like 'decimal' 
        might be considered instead of native floats. However, for general weight 
        calculations, native floats are appropriate and efficient.
    """
    return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    sample_weight_a = 50.75
    sample_weight_b = 48.23
    
    result = calculate_weight_difference(sample_weight_a, sample_weight_b)
    
    print(f"The weight difference between {sample_weight_a} and {sample_weight_b} is: {result}")