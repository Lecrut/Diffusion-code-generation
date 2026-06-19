def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    sample_side = 5
    
    result = calculate_square_area(sample_side)
    
    print(f"Side length: {sample_side}")
    print(f"Area of the square: {result}")