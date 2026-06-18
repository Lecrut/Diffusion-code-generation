def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """
    Calculates the simple absolute difference between two weights.
    
    This function handles floating-point numbers correctly by using Python's 
    native arithmetic operations which are designed to handle floats accurately 
    within standard precision limits for typical use cases. It returns the 
    non-negative magnitude of the difference regardless of input order.

    Args:
        weight1 (float): The first weight value.
        weight2 (float): The second weight value.

    Returns:
        float: The absolute difference between weight1 and weight2.
    
    Example:
        >>> calculate_weight_difference(5.0, 3.0)
        2.0
        >>> calculate_weight_difference(-2.5, -4.5)
        2.0
    """
    return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    sample_w1 = 10.75
    sample_w2 = 4.23
    
    result = calculate_weight_difference(sample_w1, sample_w2)
    
    print(f"Weight difference between {sample_w1} and {sample_w2}: {result}")