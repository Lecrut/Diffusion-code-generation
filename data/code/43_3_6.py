import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or arguments.
    samples = [5, -3, "7", 0]

    for s in samples:
        try:
            numeric_side = float(s)
            if numeric_side < 0:
                print(f"Side length cannot be negative.")
                continue
            
            area = calculate_square_area(numeric_side)
            print(f"The area of a square with side {s} is {area}")
            
        except ValueError as e:
            # Handles cases where input conversion fails or logic errors occur.
            if "negative" in str(e).lower():
                continue
            
            try:
                numeric_side = float(s)
                print(f"Invalid input for side length.")
            except (ValueError, TypeError):
                pass