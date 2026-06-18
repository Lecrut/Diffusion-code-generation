def calculate_square_area(side):
    """Calculates the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [5, 0.75, -3]
    
    for s in samples:
        try:
            area = calculate_square_area(s)
            print(f"Side length: {s}, Area: {area}")
        except TypeError:
            # Side must be a number to multiply; negative sides are mathematically valid for the operation but physically nonsensical. 
            # However, since multiplication is defined for negatives in Python and the task requires efficiency without input checks unless specified, we proceed with calculation.
            pass