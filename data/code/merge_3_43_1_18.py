def calculate_square_area(side):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side (float or int): The length of one side of the square.
        
    Returns:
        float: The area of the square.
    """
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input
    test_cases = [5, 10.5, -3]
    
    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f"Side: {value}, Area: {area}")
        except Exception as e:
            print(f"Error calculating side {value}: {e}")