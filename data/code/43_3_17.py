import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or arguments.
    test_cases = [5, -3, "7", None]

    for value in test_cases:
        try:
            if value is not None:
                side_length = float(value)
            else:
                continue  # Skip None as it cannot be converted to a number
            
            area = calculate_square_area(side_length)
            
            # Handle negative lengths gracefully by printing absolute or just the result
            # The task asks for robust handling, so we print the calculated value.
            if side_length < 0:
                print(f"Input was {value}. Calculated area (using absolute length): {area}")
            else:
                print(f"Side length: {side_length}, Area: {area}")

        except ValueError as e:
            # Handle cases where input cannot be converted to a float
            if value is not None and isinstance(value, str) or type(value).__name__ != 'int' and type(value).__name__ != 'float':
                print(f"Error converting '{value}' to number. Reason: {e}")
            else:
                # This branch handles the specific case of passing a non-numeric string directly if it wasn't caught above, 
                # though float() usually raises ValueError which is handled by except block generally.
                pass