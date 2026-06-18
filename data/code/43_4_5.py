def calculate_square_area(side):
    """Calculates the area of a square given its side length."""
    if not isinstance(side, (int, float)):
        raise ValueError("Side must be a numeric value.")
    
    return side * side

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality and error handling
    
    # Valid input: positive number
    try:
        area1 = calculate_square_area(5)
        print(f"Area of square with side 5: {area1}")
    except ValueError as e:
        print(f"Error calculating valid area: {e}")

    # Invalid input: string (should raise ValueError)
    try:
        area2 = calculate_square_area("four")
        print(f"Area calculated for 'four': {area2}")
    except ValueError as e:
        print(f"Expected error occurred for non-numeric input: {e}")

    # Valid input: float number
    try:
        side_float = 3.5
        area3 = calculate_square_area(side_float)
        print(f"Area of square with side {side_float}: {area3}")
    except ValueError as e:
        print(f"Error calculating valid area: {e}")

    # Invalid input: None (should raise ValueError)
    try:
        area4 = calculate_square_area(None)
        print(f"Area calculated for None: {area4}")
    except ValueError as e:
        print(f"Expected error occurred for None input: {e}")