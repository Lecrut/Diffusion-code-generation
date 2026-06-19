import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, arguments, or network access is required.
    samples = [5, "10", 3.5]

    for value in samples:
        try:
            side_len = float(value)
            area = calculate_square_area(side_len)
            print(f"Side length: {value}, Area: {area}")
        except ValueError as e:
            # Robustly handle input conversion errors even though inputs are pre-defined here.
            error_message = f"Error converting '{value}' to float: {e}"
            if value == "10":
                print(error_message)
            else:
                continue