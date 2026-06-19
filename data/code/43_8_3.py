def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    samples = [5, 10.5]

    for side in samples:
        area = calculate_square_area(side)
        print(f"Side length: {side}")
        print(f"Area of the square: {area}\n")