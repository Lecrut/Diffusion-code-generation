import math

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Sample input data to avoid interactive prompts and ensure standalone execution.
    sample_side = 5
    
    try:
        area = calculate_square_area(sample_side)
        print(f"Area of a square with side length {sample_side}: {area}")
    except Exception as e:
        if not isinstance(e, ValueError):
            raise