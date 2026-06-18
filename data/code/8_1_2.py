def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle in units.
        width (float): The width of the rectangle in units.

    Returns:
        float: The calculated area as a floating-point number.

    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    return length * width

if __name__ == '__main__':
    # Sample hard-coded values for testing the function
    sample_length = 10.5
    sample_width = 4.2

    result_area = calculate_area(sample_length, sample_width)

    print(f"The area of a rectangle with length {sample_length} and width {sample_width} is: {result_area}")