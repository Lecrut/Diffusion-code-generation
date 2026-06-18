def calculate_dimension_ratio(length: float, width: float) -> float:
    """
    Calculates the ratio of length to width.
    
    Args:
        length (float): The positive dimension value.
        width (float): The positive dimension value.
        
    Returns:
        float: The calculated ratio.
        
    Raises:
        ValueError: If either length or width is not positive.
    """
    if length <= 0:
        raise ValueError("Length must be a positive number.")
    if width <= 0:
        raise ValueError("Width must be a positive number.")
    
    return length / width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    test_length = 10.5
    test_width = 4.2
    
    try:
        ratio = calculate_dimension_ratio(test_length, test_width)
        print(f"Ratio of {test_length} to {test_width}: {ratio}")
        
        # Additional edge case testing with integers and floats
        int_test = calculate_dimension_ratio(100, 50)
        float_precision_test = calculate_dimension_ratio(7.89, 3.21)
        
    except ValueError as e:
        print(f"Error occurred: {e}")