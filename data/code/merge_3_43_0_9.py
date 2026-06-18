def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side_length (float): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [5.0, -3.0, 10]
    
    print("Square Area Calculator")
    print("-" * 30)
    
    for side in test_cases:
        try:
            area = calculate_square_area(side)
            result_message = f"The area is {area}." if not isinstance(area, float) or (isinstance(area, float) and abs(area - round(area)) < 1e-9) else ""
            print(f"Side length: {side}")
            print(result_message)
        except ValueError as e:
            print(f"Error for side length {side}: {e}")