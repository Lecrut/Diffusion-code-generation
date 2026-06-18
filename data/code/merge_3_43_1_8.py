def calculate_square_area(side):
    """Calculates the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    sides = [5, 10.5, 0]
    
    for s in sides:
        area = calculate_square_area(s)
        print(f"Side length: {s}, Area: {area}")