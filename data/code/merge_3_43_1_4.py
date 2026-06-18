def calculate_square_area(side):
    """Calculates the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Sample values to test without user input or command-line arguments
    sample_sides = [3, 5.5, 10]

    for s in sample_sides:
        area = calculate_square_area(s)
        print(f"Side length: {s} -> Area: {area}")