def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.

    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_length = 4.5
    sample_width = 6.2
    
    result_area = calculate_area(sample_length, sample_width)
    
    print(f"Area of rectangle with length {sample_length} and width {sample_width}: {result_area}")