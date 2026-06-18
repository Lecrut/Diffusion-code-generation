import sys

def calculate_rectangle_area(length_str: str, width_str: str) -> float:
    """Calculates the area of a rectangle given length and width as strings."""
    try:
        length = float(length_str)
        width = float(width_str)
        return length * width
    except ValueError:
        # Handle cases where input is not numeric or conversion fails
        raise

if __name__ == '__main__':
    # Hard-coded sample values to avoid any user interaction, command-line args, or file access.
    length_input = "5"
    width_input = "10"

    try:
        area = calculate_rectangle_area(length_input, width_input)
        print(f"The area of the rectangle is {area}")
    except ValueError as e:
        # This block handles potential errors from non-numeric input if sample values were different.
        print("Error calculating area:", file=sys.stderr)
        raise