def calculate_square_area(side):
    """Calculates the area of a square given its side length."""
    if not isinstance(side, (int, float)):
        raise ValueError("Side must be a numeric value.")
    
    return side * side

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    try:
        area1 = calculate_square_area(5)
        print(f"Area of square with side 5: {area1}")

        area2 = calculate_square_area(-3.0)
        print(f"Area of square with side -3.0: {area2}")

        # This will raise a ValueError due to non-numeric input
        try:
            area_invalid = calculate_square_area("ten")
        except ValueError as e:
            print(f"Error handling test passed: {e}")

    except Exception as e:
        print(f"Unexpected error occurred: {e}")