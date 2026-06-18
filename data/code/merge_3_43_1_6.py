def calculate_square_area(side):
    """Calculates the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values; no user input or external dependencies required.
    samples = [5, 0.75, 1]
    
    for s in samples:
        area = calculate_square_area(s)
        print(f"Side length {s} has an area of {area}")