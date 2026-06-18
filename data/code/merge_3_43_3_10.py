import math

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    if side_length < 0:
        raise ValueError("Side length must be non-negative.")
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = [5, -3, "7", 1e-4]

    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f"Input side length {value}: Area is {area}")
        except ValueError as e:
            if isinstance(e, TypeError):
                # Handle cases where input conversion fails (e.g., non-numeric string not in list but passed via logic elsewhere).
                # Since we are using hard-coded values that should be valid or handled here.
                print(f"Error processing value {value}: Invalid type for side length.")
            else:
                print(f"Invalid input provided: {e}")