def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    sample_side = 5.0
    
    area = calculate_square_area(sample_side)
    
    print(f"The area of the square with side length {sample_side} is: {area}")