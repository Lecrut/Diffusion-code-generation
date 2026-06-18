def calculate_area(length: float, width: float) -> float:
    """Calculates the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area as a floating-point number.
    """
    return length * width

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample_length = 5.0
    sample_width = 3.2

    result_area = calculate_area(sample_length, sample_width)

    print(f"Area: {result_area}")