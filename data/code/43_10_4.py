def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square.
        
    Returns:
        float: The calculated area of the square.
    """
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [5, -3, "invalid", None]

    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f"Side length: {value}, Area: {area}")
        except TypeError as e:
            # Gracefully handle cases where input is not a number or negative numbers if desired logic was added later
            print(f"Error calculating area for side length '{value}': Invalid value.")