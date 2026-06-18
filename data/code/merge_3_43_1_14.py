def calculate_square_area(side):
    """Calculate the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or files.
    samples = [5, 0, -3]

    for s in samples:
        print(f"Side: {s}, Area: {calculate_square_area(s)}")