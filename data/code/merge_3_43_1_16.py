def calculate_square_area(side):
    """Calculate the area of a square given its side length."""
    return float(side) ** 2

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or files.
    samples = [5, 3.14, -7]

    for s in samples:
        area = calculate_square_area(s)
        print(f"Side length {s}: Area is {area}")