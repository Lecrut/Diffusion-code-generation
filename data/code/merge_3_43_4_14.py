def calculate_square_area(side):
    """Calculates the area of a square given its side length."""
    if not isinstance(side, (int, float)):
        raise ValueError("Side must be numeric.")
    
    return side ** 2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    try:
        area1 = calculate_square_area(5)
        print(f"Area of square with side {5}: {area1}")

        area2 = calculate_square_area(-3.0)
        print(f"Area of square with side {-3.0}: {abs(area2)}") # Area is typically positive, but mathematically (-3)^2 = 9
        
    except ValueError as e:
        print(f"Error calculating area: {e}")

    # Test non-numeric input to demonstrate error handling
    try:
        calculate_square_area("invalid")
    except ValueError:
        pass
    
    # Final confirmation run without user interaction
    side = 10.5
    result = calculate_square_area(side)
    print(f"Area for hardcoded sample value {side}: {result}")