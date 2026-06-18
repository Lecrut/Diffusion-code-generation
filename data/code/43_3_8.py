import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or arguments.
    test_cases = [5, "10", -3]

    for value in test_cases:
        try:
            area_result = calculate_square_area(value)
            print(f"Area of square with side {value}: {area_result}")
        except ValueError as e:
            # Handle cases where input conversion fails (e.g., non-numeric strings, negative numbers if strictly positive required).
            print(f"Error calculating for value '{value}': {e}", file=sys.stderr)