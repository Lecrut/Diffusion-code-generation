import math

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square using direct multiplication."""
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    samples = [5.0, 123456789.0, -3.0] 
    
    print("Square Area Calculations:")
    for s in samples:
        area = calculate_square_area(s)
        if s < 0:
            print(f"Side length {s} is invalid (must be non-negative).")
        else:
            print(f"Area of square with side {s}: {area}")