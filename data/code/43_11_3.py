def calculate_square_area(side_length: float) -> float:
    """
    Calculate the area of a square given its side length.
    
    Args:
        side_length (float): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The area of the square.
        
    Raises:
        ValueError: If side_length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [5.0, -3.0, 10]
    
    print(f"Area of square with side {test_cases[0]}: {calculate_square_area(test_cases[0])}")
    try:
        result_neg = calculate_square_area(-3.0)
    except ValueError as e:
        print(f"Error for negative input: {e}")
    
    large_side = 12.5
    area_large = calculate_square_area(large_side)
    print(f"Area of square with side {large_side}: {area_large}")