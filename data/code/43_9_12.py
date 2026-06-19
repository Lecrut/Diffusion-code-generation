def calculate_square_area(side_length):
    """Calculate area of a square using direct multiplication."""
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    sides = [5, 10.5, -3]
    
    for s in sides:
        area = calculate_square_area(s)
        print(f"Side length: {s}, Area: {area}")