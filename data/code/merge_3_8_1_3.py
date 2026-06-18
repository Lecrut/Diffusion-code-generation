def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle given its length and width.

    Args:
        length (float): The length of the rectangle as a floating-point number.
        width (float): The width of the rectangle as a floating-point number.

    Returns:
        float: The calculated area, which is the product of length and width.
    """
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_length = 10.5
    sample_width = 4.2

    area = calculate_area(sample_length, sample_width)
    print(f"The area is: {area}")