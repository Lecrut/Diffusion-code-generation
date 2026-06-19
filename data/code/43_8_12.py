def calculate_square_area(side_length):
    """Calculates the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, or argparse)
    samples = [5.0, 10]

    for s in samples:
        area = calculate_square_area(s)
        print(f"Side length: {s}")
        print(f"Area of the square: {area}\n")