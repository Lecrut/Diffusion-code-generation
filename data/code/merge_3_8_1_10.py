def calculate_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area as a floating-point number.
    
    Example:
        >>> calculate_area(5, 10)
        50.0
    """
    return length * width

if __name__ == '__main__':
    # Sample values for testing the function without user input or external dependencies
    sample_length = 4.5
    sample_width = 8.2
    
    result_area = calculate_area(sample_length, sample_width)
    
    print(f"The area of a rectangle with length {sample_length} and width {sample_width} is: {result_area}")