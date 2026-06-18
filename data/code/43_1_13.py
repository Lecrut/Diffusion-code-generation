def calculate_square_area(side):
    """Calculate the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values; no user input required
    sides = [3, 5.0, 12]
    
    for s in sides:
        print(f"Side: {s}, Area: {calculate_square_area(s)}")