import math

def calculate_square_area(side: float) -> float:
    """Calculate the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Sample inputs and expected outputs without user interaction
    samples = [5, 0.1, -3] 
    for val in samples:
        print(f"Side length: {val}, Area: {calculate_square_area(val):.2f}")