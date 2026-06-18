import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required.
    # Simulating robust input handling by testing with pre-defined strings.
    test_cases = [
        "5",      # Valid integer string
        "-3.5",   # Negative float (valid mathematically, though side length usually positive)
        "10"
    ]

    for case in test_cases:
        try:
            # Attempt to convert the input string to a float/integer robustly
            area = calculate_square_area(float(case))
            print(f"Side length: {case}, Area: {area}")
        except ValueError as e:
            # Handle cases where conversion fails (though our test cases are valid)
            print(f"Error processing input '{case}': {e}", file=sys.stderr)