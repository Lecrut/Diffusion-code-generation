def calculate_square_area(side):
    """Calculates the area of a square given its side length.
    
    Args:
        side (int | float): The length of one side of the square.
        
    Returns:
        int | float: The calculated area of the square.
        
    Raises:
        ValueError: If 'side' is not an integer or a numeric type that can be converted to float.
    """
    if isinstance(side, (int, float)) and not isinstance(side, bool):
        return side * side
    else:
        raise ValueError("Input must be a number.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    try:
        result = calculate_square_area(5)
        print(f"Area of square with side 5: {result}")
        
        result2 = calculate_square_area(3.5)
        print(f"Area of square with side 3.5: {result2}")
        
        # This will raise a ValueError as expected
        try:
            invalid_result = calculate_square_area("invalid")
        except ValueError as e:
            print(f"Caught error for non-numeric input: {e}")
            
    except Exception as e:
        print(f"Unexpected error occurred: {e}")