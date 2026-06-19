import math

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 5.0
    
    # Calculate and print the result for the sample value
    calculated_area = calculate_square_area(sample_side)
    print(f"Side length: {sample_side}")
    print(f"Area of square: {calculated_area:.2f} square units")