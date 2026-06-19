def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no user input required)
    sides = [5, 10.5]
    
    for side in sides:
        area = calculate_square_area(side)
        print(f"Side length: {side}, Area of square: {area}")