def calculate_weight_difference(weight1: float | None, weight2: float | None) -> float:
    """
    Calculate the absolute simple weight difference between two given weights.
    
    This function handles floating-point numbers correctly by using a small 
    epsilon value for comparison if needed in future extensions, though currently
    it performs standard arithmetic which is sufficient for simple differences.
    
    If either input is None or not a number, the function raises a TypeError.
    
    Args:
        weight1 (float): The first weight value. Can be positive, negative, zero, 
                        or float. Floating-point precision issues are inherent to 
                        binary representation but standard arithmetic handles them as per Python specs.
        weight2 (float): The second weight value. Same constraints as weight1.
    
    Returns:
        float: The absolute difference between the two weights.
        
    Raises:
        TypeError: If either input is not a numeric type or is None.
    
    Examples:
        >>> calculate_weight_difference(5, 3)
        2.0
        >>> calculate_weight_difference(-1.5, -4.5)
        3.0
        
    Note:
        The function uses the built-in abs() function to ensure a positive difference 
        and standard float operations which are precise enough for general weight calculations 
        within typical application ranges (e.g., grams up to astronomical scales)."""
    
    # Validate input types and values
    if not isinstance(weight1, (int, float)):
        raise TypeError(f"weight1 must be a number, got {type(weight1).__name__}")
    
    if weight1 is None:
        raise TypeError("Cannot calculate difference with null value")
    
    if not isinstance(weight2, (int, float)):
        raise TypeError(f"weight2 must be a number, got {type(weight2).__name__}")
    
    if weight2 is None:
        raise TypeError("Cannot calculate difference with null value")

    # Perform the calculation using standard arithmetic to maintain Python's precision guarantees for floats/integers
    
    return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, network access, or file dependencies are required.
    # These samples cover integers and floating-point numbers with varying magnitudes to test robustness.
    
    val_a = 50.75
    val_b = -12.3
    
    difference_result = calculate_weight_difference(val_a, val_b)

    print(f"Weight Difference between {val_a} and {val_b}:")
    print(difference_result)