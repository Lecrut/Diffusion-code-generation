import math

def calculate_square_area(side_length):
    """Calculates the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    test_cases = [5.0, 10]
    
    for side in test_cases:
        area = calculate_square_area(side)
        print(f"Side length: {side}")
        print(f"Area of the square: {area:.2f}\n")