def calculate_square_area(side_length):
    """Calculate the area of a square using side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [5, 10.5, 0]
    
    for s in samples:
        area = calculate_square_area(s)
        print(f"Side length: {s}, Area: {area}")