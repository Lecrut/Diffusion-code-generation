def calculate_area(length: float | int, width: float | int) -> float:
    """
    Calculate the area of a rectangle given its length and width.

    Args:
        length (float | int): The length of the rectangle.
        width (float | int): The width of the rectangle.

    Returns:
        float: The calculated area as a floating-point number.
    
    Example:
        >>> calculate_area(5, 10)
        50.0
    """
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_length = 4.5
    test_width = 6
    
    area_result = calculate_area(test_length, test_width)
    
    print(f"The area of a rectangle with length {test_length} and width {test_width} is: {area_result}")