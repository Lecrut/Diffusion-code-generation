def calculate_dimension_ratio(length: float, width: float) -> float:
    """
    Calculates the ratio between two dimensions (length / width).
    
    Args:
        length (float): The first dimension value. Must be positive.
        width (float): The second dimension value. Must be positive.
        
    Returns:
        float: The calculated ratio of length to width.
        
    Raises:
        ValueError: If either length or width is not a positive number.
    """
    if length <= 0:
        raise ValueError("Length must be a positive number.")
    if width <= 0:
        raise ValueError("Width must be a positive number.")
    
    return length / width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_length = 12.5
    test_width = 8.0
    
    try:
        ratio = calculate_dimension_ratio(test_length, test_width)
        print(f"Ratio of {test_length} to {test_width}: {ratio}")
        
        # Additional edge case tests within the main block for completeness
        negative_test_cases = [(-5.0, 10.0), (5.0, -3.0)]
        zero_tests = [(0.0, 4.0), (6.0, 0.0)]
        
        print("\nTesting error handling:")
        for val in negative_test_cases:
            try:
                calculate_dimension_ratio(*val)
            except ValueError as e:
                print(f"Caught expected error for {val}: {e}")
                
        for val in zero_tests:
            try:
                calculate_dimension_ratio(*val)
            except ValueError as e:
                print(f"Caught expected error for {val}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")