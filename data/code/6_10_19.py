def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """
    Calculates the simple absolute difference between two weights.
    
    This function handles floating-point numbers correctly by using Python's 
    native arithmetic operations which are designed to handle floats accurately 
    within standard precision limits for typical use cases. It returns the 
    non-negative difference regardless of input order.

    Args:
        weight1 (float): The first weight value.
        weight2 (float): The second weight value.

    Returns:
        float: The absolute difference between weight1 and weight2.
    
    Example:
        >>> calculate_weight_difference(5.0, 3.0)
        2.0
        >>> calculate_weight_difference(-1.5, -4.5)
        3.0
    
    Note:
        Floating-point arithmetic in Python follows IEEE 754 standards. 
        For extremely high precision requirements beyond standard float64, 
        the decimal module or fractions.Fraction could be considered instead.
    """
    return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    sample_weight_a = 10.5
    sample_weight_b = 7.3
    
    result = calculate_weight_difference(sample_weight_a, sample_weight_b)
    
    print(f"Weight A: {sample_weight_a}")
    print(f"Weight B: {sample_weight_b}")
    print(f"Difference: {result}")