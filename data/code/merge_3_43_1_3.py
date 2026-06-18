def calculate_square_area(side):
    """Calculate the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or external dependencies
    samples = [1, 5.0, 10]

    for s in samples:
        area = calculate_square_area(s)
        print(f"Side length {s} has an area of {area}")