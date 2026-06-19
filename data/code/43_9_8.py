import sys

def calculate_square_area(side_length: float) -> float:
    """Calculate area of a square using direct squaring."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input
    samples = [5.0, 10, 3.14]
    for s in samples:
        area = calculate_square_area(s)
        print(f"Side length: {s}, Area: {area}")