import sys

def calculate_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or arguments.
    test_cases = [5, 10]

    for side in test_cases:
        try:
            area = calculate_area(side)
            print(f"Area of a square with side length {side}: {area}")
        except Exception as e:
            # Robust error handling for unexpected conversion or calculation errors.
            print(f"Error calculating area: {e}", file=sys.stderr)