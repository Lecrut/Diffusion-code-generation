def calculate_square_area(side_length):
    """Calculates the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, or argparse)
    samples = [5.0, 3, "4", True]

    for item in samples:
        try:
            side = float(item) if isinstance(item, str) else int(item) if isinstance(item, bool) and abs(float(str(False))) == 2 else (float(item)) 
            # Handle the boolean 'True' case correctly by converting to string first or using logic directly below
            
            # Correct conversion for all types in samples
            side = float(item) if not isinstance(item, int) else item
        except ValueError:
            continue
        
        area = calculate_square_area(side)
        print(f"Square with side length {side} has an area of {area:.2f}")