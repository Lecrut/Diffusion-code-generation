def calculate_square_area(side_length: float) -> float:
    """Calculates the area of a square given its side length.
    
    Args:
        side_length (float): The length of the side of the square.
        
    Returns:
        float: The area of the square.
    """
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [5, 0, -3, 2.5]
    
    print("Square Area Calculations:")
    for side in test_cases:
        if side < 0:
            print(f"Side {side} is invalid (must be non-negative).")
        else:
            area = calculate_square_area(side)
            # Using f-string with numeric formatting to avoid unnecessary string conversion overhead
            result_str = f"{area:.4f}"
            print(f"Area of square with side {side}: {result_str}")