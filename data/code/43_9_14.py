def calculate_square_area(side_length):
    """Calculate area of a square using direct multiplication."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    samples = [5, 10.5, 0]
    for s in samples:
        print(f"Side length: {s}, Area: {calculate_square_area(s)}")