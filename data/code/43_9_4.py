import math

def calculate_square_area(side_length):
    """Calculate area of a square using direct multiplication."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    samples = [5.0, 10, -3]  # Includes edge case for negative number (mathematically valid in code)
    
    print("Square Area Calculations:")
    for side in samples:
        area = calculate_square_area(side)
        if isinstance(side, int):
            print(f"Side {side}: Area is {area}")
        else:
            print(f"Side {side:.2f}: Area is {area:.4f}")