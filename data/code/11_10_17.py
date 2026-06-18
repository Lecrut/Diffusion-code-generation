def calculate_length_ratio(length_a: float, length_b: float) -> float | None:
    """
    Calculates the ratio of two given lengths (length_a / length_b).
    
    Args:
        length_a (float): The numerator length.
        length_b (float): The denominator length.
        
    Returns:
        float or None: The calculated ratio if successful, otherwise None 
                      in case of division by zero to avoid runtime errors.
                      
    Raises:
        ValueError: If either input is not a numeric value.
    """
    try:
        # Ensure inputs are numbers (integers and floats)
        length_a = float(length_a)
        length_b = float(length_b)
        
        if length_b == 0:
            return None
        
        ratio = length_a / length_b
        return ratio
    
    except TypeError as e:
        # Handle cases where inputs are not convertible to numbers
        raise ValueError(f"Inputs must be numeric values. Error details: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    length_1 = 20.5
    length_2 = 4

    try:
        result_ratio = calculate_length_ratio(length_1, length_2)
        
        if result_ratio is not None:
            print(f"Ratio of {length_1} to {length_2}: {result_ratio}")
        else:
            print("Error: Division by zero encountered.")
    except ValueError as e:
        # Catch any potential type conversion errors during execution
        print(f"Invalid input provided. Please ensure values are numbers.\n{e}")

    # Test case for division by zero scenario (graceful handling)
    length_3 = 10
    length_4 = 0
    
    try:
        result_ratio_zero_division = calculate_length_ratio(length_3, length_4)
        
        if result_ratio_zero_division is None:
            print("Test case passed for division by zero. Function returned None instead of crashing.")
        else:
            print(f"Unexpected ratio value for zero denominator: {result_ratio_zero_division}")
    except ValueError as e:
        # This block should not be reached because the function handles it internally, 
        # but included here to demonstrate robustness against external type errors.
        print(f"An unexpected error occurred in test case 2.\n{e}")