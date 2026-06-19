import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, or network access is required.
    test_cases = [5.0, "10", "-3"]

    for value in test_cases:
        try:
            side_length = float(value)
            area = calculate_square_area(side_length)
            print(f"Side length: {value}, Area: {area}")
        except ValueError as e:
            # Handle cases where conversion to float fails (e.g., non-numeric input or negative numbers if strictly positive is required, though mathematically square side can be any real number).
            # The task asks for robust handling; printing the error message demonstrates this.
            print(f"Error converting '{value}' to a valid numeric value: {e}")