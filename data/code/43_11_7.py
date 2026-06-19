def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square.
        
    Returns:
        float: The area of the square.
        
    Raises:
        TypeError: If side_length is not a numeric type.
        ValueError: If side_length is negative.
    """
    if isinstance(side_length, (int, float)) and not isinstance(side_length, bool):
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        return side_length ** 2
    else:
        raise TypeError("side_length must be a number.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [5, -3.0, "invalid", True]
    
    for value in sample_cases:
        try:
            result = calculate_square_area(value)
            print(f"Side length {value}: Area is {result}")
        except (TypeError, ValueError) as e:
            print(f"Error processing side length {value}: {e}")