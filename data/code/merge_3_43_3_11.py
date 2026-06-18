import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or network access is required.
    # Simulating robust input handling by testing with pre-defined strings and floats.
    
    test_cases = [
        "5",      # Valid integer string
        3.14,     # Direct float value (simulating parsed output)
        "-2",     # Negative number to verify calculation logic holds
    ]

    for side_str in test_cases:
        try:
            if isinstance(side_str, str):
                area = calculate_square_area(float(side_str))
            else:
                area = calculate_square_area(side_str)
            
            print(f"Side length: {side_str}, Area: {area}")
        except ValueError as e:
            # Handles cases where conversion fails (though test_cases are valid here)
            print(f"Error converting input '{side_str}': {e}", file=sys.stderr)