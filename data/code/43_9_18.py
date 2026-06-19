def calculate_square_area(side):
    """Calculate the area of a square using direct multiplication."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values to run without user input
    test_side = 5.0
    
    result = calculate_square_area(test_side)
    
    print(f"Area for a square with side length {test_side}: {result}")