def calculate_square_area(side_length):
    """Calculates the area of a square given its side length.
    
    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side_length is negative.
    """
    if isinstance(side_length, (int, float)):
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        return side_length ** 2
    else:
        raise TypeError(f"Expected a number, got {type(side_length).__name__}.")

if __name__ == '__main__':
    # Sample test cases to verify functionality without user input or external dependencies.
    sample_values = [5, -3.0, 100]

    for value in sample_values:
        try:
            area = calculate_square_area(value)
            print(f"Side length {value}: Area is {area}")
        except ValueError as ve:
            print(f"Error for side length {value}: {ve}")