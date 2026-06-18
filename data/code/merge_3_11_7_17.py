def calculate_dimension_ratio(length: float, width: float) -> float:
    """
    Calculates the ratio between two dimensions (length/width).
    
    Args:
        length (float): The first dimension value. Must be positive.
        width (float): The second dimension value. Must be positive.
        
    Returns:
        float: The calculated ratio of length to width.
        
    Raises:
        ValueError: If either input is not a number or if it is less than or equal to zero.
    
    Examples:
        >>> calculate_dimension_ratio(10, 5)
        2.0
        
        >>> calculate_dimension_ratio(-3, 4)
        Traceback (most recent call last):
            ...
        ValueError: Both dimensions must be positive numbers.
        
        >>> calculate_dimension_ratio(None, None)
        Traceback (most recent call last):
            ...
        TypeError: Inputs must be numeric values.
    """
    
    # Validate input types and constraints
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Inputs must be numeric values.")
        
    if length <= 0 or width <= 0:
        raise ValueError("Both dimensions must be positive numbers.")

    return length / width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    try:
        result = calculate_dimension_ratio(12.5, 4)
        print(f"Ratio of {12.5} to {4}: {result}")
        
        # Additional test case with integers
        ratio_ints = calculate_dimension_ratio(100, 7)
        print(f"Integer Ratio: {ratio_ints:.2f}")
        
    except ValueError as ve:
        print(f"Value Error encountered: {ve}")
    except TypeError as te:
        print(f"Type Error encountered: {te}")