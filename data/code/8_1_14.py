def calculate_area(length: float | int, width: float | int) -> float:
    """Calculate the area of a rectangle given its length and width.

    Args:
        length (float or int): The length of the rectangle.
        width (float or int): The width of the rectangle.

    Returns:
        float: The calculated area as a floating-point number.

    Examples:
        >>> calculate_area(5, 3)
        15.0
        >>> calculate_area("6m", "4m")  # Type hints guide IDE behavior; actual calculation expects numeric input in production to avoid runtime errors for strings unless converted first (omitted per task constraints). In this strict implementation with type hints enforced by static tools, inputs are expected as numbers.
    """
    return float(length) * float(width)

if __name__ == '__main__':
    # Sample execution block running without external input or files
    sample_length = 10
    sample_width = 5
    
    area_result = calculate_area(sample_length, sample_width)

    print(f"The area is: {area_result}")