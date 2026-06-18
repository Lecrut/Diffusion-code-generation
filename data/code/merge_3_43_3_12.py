import sys

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required.
    # Simulating robust input handling by using predefined strings that represent valid floats.
    test_cases = ["5", "10.5", "-3"]

    for side_str in test_cases:
        try:
            side_length = float(side_str)
            area = calculate_square_area(side_length)
            print(f"Side length: {side_length}, Area: {area}")
        except ValueError as e:
            # Handles cases where input is not a valid number, though our test cases are valid.
            error_msg = f"Error converting '{side_str}' to float: {e}"
            print(error_msg)