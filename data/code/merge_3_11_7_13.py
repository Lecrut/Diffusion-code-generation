def calculate_dimension_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio between two dimensions (length1 / length2).
    
    Args:
        length1 (float): The first dimension value. Must be positive.
        length2 (float): The second dimension value. Must be positive.
        
    Returns:
        float: The ratio of length1 to length2.
        
    Raises:
        ValueError: If either input is not a number or if it is zero or negative.
    """
    
    # Validate that both inputs are numbers (floats) and strictly positive
    try:
        num1 = float(length1)
        num2 = float(length2)
        
        if isinstance(num1, bool):  # Check for boolean first since bool is subclass of int in Python
            raise ValueError("Inputs must be numeric floats.")
            
        if not (num1 > 0 and num2 > 0):
            raise ValueError(f"Both dimensions must be strictly positive. Received: length1={length1}, length2={length2}")
        
    except TypeError as e:
        raise ValueError(f"Invalid input type or value, both must be numeric floats.") from e
        
    # Calculate the ratio safely since we've verified non-zero denominator
    return num1 / num2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    dim_a = 10.5
    dim_b = 3
    
    try:
        result = calculate_dimension_ratio(dim_a, dim_b)
        print(f"The ratio of {dim_a} to {dim_b} is: {result}")
        
        # Test edge case handling with invalid inputs (commented out for single run cleanliness if desired, 
        # but kept in scope to demonstrate error logic could be tested separately if needed).
        # For this specific task requirement ("run without user input"), we just print the successful result.
    except ValueError as ve:
        print(f"Error occurred during calculation: {ve}")