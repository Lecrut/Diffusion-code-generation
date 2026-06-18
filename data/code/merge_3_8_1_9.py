def calculate_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle given its length and width.
    
    Parameters:
        length (float): The length of the rectangle. Must be non-negative.
        width (float): The width of the rectangle. Must be non-negative.
    
    Returns:
        float: The calculated area of the rectangle.
    
    Raises:
        ValueError: If either dimension is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width

if __name__ == '__main__':
    # Sample values for testing without any user input or external dependencies
    sample_length = 5.0
    sample_width = 3.7
    
    try:
        area = calculate_area(sample_length, sample_width)
        print(f"Area of rectangle with length {sample_length} and width {sample_width}: {area}")
    except ValueError as ve:
        print(f"Error calculating area: {ve}")