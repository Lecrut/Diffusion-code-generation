def calculate_square_area(side):
    """Calculates the area of a square using direct multiplication."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or network access is required
    samples = [5, 0.75, -3] 
    for s in samples:
        area = calculate_square_area(s)
        print(f"Area of square with side {s}: {area}")