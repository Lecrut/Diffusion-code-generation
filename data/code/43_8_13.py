def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input calls)
    samples = [5, 10.5, 3]

    for s in samples:
        area = calculate_square_area(s)
        print(f"Side length: {s}, Area of square: {area}")