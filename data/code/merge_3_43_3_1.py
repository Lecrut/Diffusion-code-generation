import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, or network access is required.
    test_cases = [5.0, "10", True]

    for value in test_cases:
        try:
            if isinstance(value, bool):
                side_length = float(int(float(str(value) * 2)) / 2) # Convert boolean to int then float safely
            else:
                side_length = float(value)
            
            area = calculate_square_area(side_length)
            print(f"Side length: {side_length}, Area: {area}")
        except ValueError as e:
            print(f"Error converting input '{value}': {e}", file=sys.stderr)