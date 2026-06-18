def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """
    Calculates the absolute simple difference between two weights.
    
    This function takes two floating-point numbers representing weights
    and returns their absolute difference as a new floating-point number.
    
    Args:
        weight1 (float): The first weight value.
        weight2 (float): The second weight value.
        
    Returns:
        float: The absolute difference between the two weights.
        
    Example:
        >>> calculate_weight_difference(50.5, 49.8)
        0.7
    
    Note:
        Floating-point arithmetic may introduce minor precision errors,
        but this function performs a standard subtraction followed by
        an absolute value operation to ensure the result is non-negative.
    
    Raises:
        TypeError: If either weight1 or weight2 is not a float or int.
    """
    if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
        raise TypeError("Both weights must be numeric types.")

    return abs(float(weight1) - float(weight2))

if __name__ == '__main__':
    # Sample values for testing the function without user input.
    sample_weight_a = 50.75
    sample_weight_b = 49.83
    
    difference = calculate_weight_difference(sample_weight_a, sample_weight_b)
    
    print(f"Weight A: {sample_weight_a}")
    print(f"Weight B: {sample_weight_b}")
    print(f"Difference: {difference}")