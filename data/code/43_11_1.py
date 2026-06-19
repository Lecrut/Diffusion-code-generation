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
    
    print(f"Side length: {test_cases[0]}, Area: {calculate_square_area(test_cases[0])}")
    try:
        result = calculate_square_area(-3.0)
    except ValueError as e:
        print(f"Error for negative input: {e}")
        
    side_length_10 = 10
    area_10 = calculate_square_area(side_length_10)
    print(f"Side length: {side_length_10}, Area: {area_10}")