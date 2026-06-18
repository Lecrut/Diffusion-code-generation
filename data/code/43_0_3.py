def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    The formula used is: Area = side * side
    
    Args:
        side_length (float or int): The length of one side of the square.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
    
    Examples:
        >>> calculate_square_area(5)
        25.0
        >>> calculate_square_area(-3)
        Traceback (most recent call last):
            ...
        ValueError: Side length must be non-negative.
    """
    if side_length < 0:
        raise ValueError("Side length must be non-negative.")
    
    return float(side_length * side_length)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [5, 10, 2.5]

    print("Calculating areas of squares with the following side lengths:")
    
    for side in test_cases:
        try:
            area = calculate_square_area(side)
            print(f"Side length: {side} -> Area: {area}")
        except ValueError as e:
            print(f"Error calculating area for side {side}: {e}")