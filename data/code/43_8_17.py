def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies.
    samples = [5, 10.5, 1]

    for s in samples:
        area = calculate_square_area(s)
        print(f"Side length: {s}, Area of square: {area}")