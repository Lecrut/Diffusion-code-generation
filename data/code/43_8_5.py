import math

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 5
    
    # Hard-coded calculation for testing without input() calls
    calculated_area = calculate_square_area(sample_side)
    
    print(f"Area of the square with side length {sample_side}:")
    print(calculated_area)