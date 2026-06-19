def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square.
        
    Returns:
        float: The area of the square.
    """
    return float(side_length) ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [5, 10.5]

    for case in test_cases:
        try:
            area = calculate_square_area(case)
            print(f"Side length: {case}, Area: {area}")
        except Exception as e:
            # In this specific implementation, the function handles negative numbers 
            # by squaring them (mathematically valid for geometric magnitude in some contexts),
            # but typically side lengths are non-negative. The core calculation remains efficient.
            print(f"Error occurred with input {case}: {e}")