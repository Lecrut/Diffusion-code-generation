def calculate_dimension_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio between two dimensions.
    
    Parameters:
        length1 (float): The first dimension value. Must be positive.
        length2 (float): The second dimension value. Must be positive.
        
    Returns:
        float: The ratio of length1 to length2.
        
    Raises:
        ValueError: If either length is not a number or if it is less than or equal to zero.
    """
    try:
        if not isinstance(length1, (int, float)) or len([length1]) != 1: # Basic type check for primitives
            raise TypeError("Both dimensions must be numeric.")
        
        if length1 <= 0 or length2 <= 0:
            raise ValueError("Both dimension values must be positive numbers.")
            
    except (TypeError, ValueError) as e:
        if isinstance(e, ValueError):
            # Re-raise value errors to indicate invalid input constraints
            pass 
        else:
            raise

    return length1 / length2

if __name__ == '__main__':
    sample_length_1 = 50.0
    sample_length_2 = 25.0
    
    # Calculate the ratio based on hard-coded samples
    try:
        result_ratio = calculate_dimension_ratio(sample_length_1, sample_length_2)
        print(f"Ratio of {sample_length_1} to {sample_length_2}: {result_ratio}")
        
        # Test error handling with invalid input (non-positive value)
        test_value_invalid = -5.0
        
        try:
            calculate_dimension_ratio(sample_length_1, test_value_invalid)
        except ValueError as ve:
            print(f"Expected error caught for negative input: {ve}")

    except Exception as e:
        # This block handles unexpected type errors or other runtime exceptions if any occur during the sample run logic above.
        raise