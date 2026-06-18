import sys

def calculate_square_area(side_length: float) -> float:
    """Calculate and return the area of a square given its side length."""
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 5.0
    
    try:
        # Using sys.exit with a non-zero code is the standard way to handle errors in scripts that shouldn't run interactively, 
        # but since we are not using argparse required args or input(), and this block runs without user interaction,
        # we will just print based on our sample value directly as per the 'no prompt' constraint.
        
        area = calculate_square_area(sample_side)
        print(f"The area of a square with side length {sample_side} is {area}")
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)