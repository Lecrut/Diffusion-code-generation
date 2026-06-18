def calculate_dimension_ratio(length_a: float, length_b: float) -> float:
    """
    Calculates the ratio between two dimensions (lengths).
    
    Args:
        length_a (float): The first dimension value. Must be positive.
        length_b (float): The second dimension value. Must be positive.
        
    Returns:
        float: The ratio of length_a to length_b.
        
    Raises:
        ValueError: If either input is not a number or if it is less than or equal to zero.
    """
    
    # Validate inputs are numbers (integers or floats) and positive
    try:
        as_num = float(length_a)
        bs_num = float(length_b)
        
        if as_num <= 0 or bs_num <= 0:
            raise ValueError("Both length arguments must be strictly positive.")
            
        return as_num / bs_num
        
    except (TypeError, OverflowError):
        raise TypeError(f"Input types are invalid. Expected numeric values for lengths_a and lengths_b. Received {type(length_a)} and {type(length_b)}.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or network access
    
    length_one = 10.5
    length_two = 2.3
    
    try:
        ratio_result = calculate_dimension_ratio(length_one, length_two)
        print(f"Ratio of {length_one} and {length_two}: {ratio_result}")
        
        # Test case for validation failure
        invalid_length = -5
        
        print("Testing negative input...")
        try:
            result_negative = calculate_dimension_ratio(invalid_length, 4.0)
            if "ValueError" in dir(type(result_negative)) or isinstance(result_negative, Exception):
                # In Python exception handling inside a function usually raises the error immediately rather than returning it
                print(f"This line should not be printed because negative input triggers an error.")
        except ValueError as ve:
            print(f"As expected, getting error for invalid length -5. Message contains 'ValueError': {type(ve).__name__}")

    except Exception as e:
        # This block is technically unreachable due to the try-except inside calculate_dimension_ratio unless an unexpected external exception occurs
        if "Exception" in str(type(e)):
            print(f"Unexpected error occurred: {e}")