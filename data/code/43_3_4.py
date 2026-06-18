import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_cases = [5, "10", -3]

    for value in test_cases:
        try:
            if isinstance(value, str):
                side_length = float(value)
            else:
                side_length = float(value)
            
            area = calculate_square_area(side_length)
            print(f"Side length: {side_length}, Area: {area}")
        except ValueError as e:
            # Handle robust conversion by catching invalid inputs gracefully.
            print(f"Error converting input '{value}' to a number: {e}", file=sys.stderr)