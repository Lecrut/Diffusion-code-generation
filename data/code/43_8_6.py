def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Sample values to test without user input or external dependencies
    sample_side = 5
    
    result = calculate_square_area(sample_side)
    
    print(f"The area is: {result}")