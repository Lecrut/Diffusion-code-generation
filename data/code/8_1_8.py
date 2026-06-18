def calculate_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle. Must be non-negative.
        width (float): The width of the rectangle. Must be non-negative.

    Returns:
        float: The calculated area as the product of length and width.

    Raises:
        ValueError: If either dimension is negative or not a number.
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numeric.")
    
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")

    return length * width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    sample_length = 5.0
    sample_width = 10
    
    result_area = calculate_area(sample_length, sample_width)
    
    print(f"Area of rectangle with length {sample_length} and width {sample_width}:")
    print(result_area)