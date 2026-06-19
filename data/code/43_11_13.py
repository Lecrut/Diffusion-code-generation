def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [5, -3.5, 10]

    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f"Side length {value}: Area is {area}")
        except ValueError as e:
            print(f"Error for side length {value}: {e}")