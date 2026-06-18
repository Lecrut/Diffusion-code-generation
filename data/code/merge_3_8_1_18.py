def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area as product of length and width.
    
    Raises:
        ValueError: If either dimension is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_length = 5.0
    test_width = 3.2
    
    area_result = calculate_area(test_length, test_width)
    
    print(f"Area of rectangle with length {test_length} and width {test_width}:")
    print(f"{area_result}")