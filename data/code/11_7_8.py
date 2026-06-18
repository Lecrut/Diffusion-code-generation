def calculate_dimension_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio between two dimensions (length1 / length2).
    
    Args:
        length1 (float): The first dimension value. Must be positive.
        length2 (float): The second dimension value. Must be positive.
        
    Returns:
        float: The ratio of length1 to length2.
        
    Raises:
        ValueError: If either length is not a positive number.
    """
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive numbers.")
    
    return length1 / length2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    dim_a = 10.5
    dim_b = 3
    
    try:
        ratio = calculate_dimension_ratio(dim_a, dim_b)
        print(f"Ratio of {dim_a} to {dim_b}: {ratio}")
        
        # Additional test case with different values
        ratio2 = calculate_dimension_ratio(100, 50)
        print(f"Ratio of 100 to 50: {ratio2}")
    except ValueError as e:
        print(f"Error encountered: {e}")