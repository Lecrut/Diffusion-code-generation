def calculate_square_area(side_length):
    """Calculate the area of a square efficiently."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    samples = [5, 10.5, 1]
    
    for length in samples:
        area = calculate_square_area(length)
        print(f"Area of square with side {length}: {area}")