def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle given its length and width."""
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative numbers.")
    return length * width

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input.
    sample_length = 12.5
    sample_width = 8.3

    try:
        area = calculate_rectangle_area(sample_length, sample_width)
        print(f"The area of a rectangle with length {sample_length} and width {sample_width} is {area}.")
    except ValueError as e:
        print(f"Error calculating area: {e}")