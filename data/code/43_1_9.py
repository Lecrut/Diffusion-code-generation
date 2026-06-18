def calculate_square_area(side):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The area of the square, calculated as side^2.
        
    Raises:
        ValueError: If 'side' is negative.
    """
    if side < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_sides = [5, -3.5, 0]
    
    for s in test_sides:
        try:
            area = calculate_square_area(s)
            print(f"Side {s}: Area is {area}")
        except ValueError as e:
            print(f"Error for side {s}: {e}")