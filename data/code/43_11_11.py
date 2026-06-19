def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        TypeError: If side_length is not a number.
        ValueError: If side_length is negative.
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be an integer or float.")
    
    if side_length < 0:
        raise ValueError("side_length cannot be negative.")
        
    return side_length ** 2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [5, -3.5, "invalid", (4,), []]

    for val in samples:
        try:
            result = calculate_square_area(val)
            print(f"Input {val} -> Area: {result}")
        except Exception as e:
            print(f"Error processing input {val}: {type(e).__name__}: {e}")