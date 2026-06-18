from typing import Union

def calculate_square_area(side: float) -> float:
    """Calculate the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [5.0, 123456789]
    
    for s in samples:
        area = calculate_square_area(s)
        print(f"Side length: {s}, Area: {area}")