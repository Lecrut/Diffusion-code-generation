import sys

def calculate_rectangle_area(length: str, width: str) -> float:
    """Calculate the area of a rectangle given length and width as strings."""
    try:
        l = float(length)
        w = float(width)
        return l * w
    except ValueError:
        raise ValueError("Length and width must be numeric values.")

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without input.
    sample_length_str = "10"
    sample_width_str = "5"

    try:
        area_value = calculate_rectangle_area(sample_length_str, sample_width_str)
        print(f"The area of the rectangle is {area_value}")
    except ValueError as e:
        print(str(e), file=sys.stderr)