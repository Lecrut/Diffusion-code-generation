def get_square_area(side_length):
    """Calculate and return the area of a square given its side length."""
    if isinstance(side_length, (int, float)):
        try:
            numeric_side = float(side_length)
            if numeric_side < 0:
                raise ValueError("Side length cannot be negative.")
            return numeric_side ** 2
        except Exception as e:
            print(f"Error converting input to number: {e}")
            return None
    else:
        print("Input must be a valid number (int or float).")
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [5, -3.0, "7", 10]
    
    for side in test_cases:
        area_result = get_square_area(side)
        if area_result is not None:
            print(f"Area of square with side {side}: {area_result}")