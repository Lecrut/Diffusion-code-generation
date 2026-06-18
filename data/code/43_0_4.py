def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
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
    test_cases = [5.0, 10, -3]

    print("Square Area Calculator")
    print("-" * 20)

    for side in test_cases:
        try:
            area = calculate_square_area(side)
            print(f"Side length: {side}")
            print(f"Area: {area}\n")
        except ValueError as e:
            print(f"Error calculating area for side {side}: {e}\n")