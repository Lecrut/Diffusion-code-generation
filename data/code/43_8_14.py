def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Sample values to test without user input or command-line arguments
    sample_sides = [5, 10.5]

    for side in sample_sides:
        area = calculate_square_area(side)
        print(f"Side length: {side}")
        print(f"Area of the square: {area}\n")