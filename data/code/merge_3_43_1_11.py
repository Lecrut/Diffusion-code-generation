def calculate_square_area(side):
    """Calculate the area of a square given its side length."""
    return side * side

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    samples = [5, 0.75, -3]

    for s in samples:
        try:
            area = calculate_square_area(s)
            print(f"Side: {s}, Area: {area}")
        except Exception as e:
            # Handle invalid inputs like negative sides if necessary, though mathematically valid
            print(f"Error calculating side {s}: {e}")