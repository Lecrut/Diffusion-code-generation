def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square.
        
    Returns:
        float: The calculated area of the square.
    """
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [5, 10.5, -3]

    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f"Side length: {value}, Area: {area}")
        except TypeError as e:
            # Optional error handling if non-numeric input is passed unexpectedly
            print(f"Error calculating area for side length {value}: {e}")