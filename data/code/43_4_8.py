def calculate_square_area(side):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side (numeric): The length of one side of the square.
        
    Returns:
        float or int: The calculated area of the square.
        
    Raises:
        ValueError: If 'side' is not a numeric type.
    """
    if not isinstance(side, (int, float)):
        raise ValueError("Input must be a number.")
    
    return side * side

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    print(f"Area of square with side 5: {calculate_square_area(5)}")
    
    try:
        result = calculate_square_area("invalid")
    except ValueError as e:
        print(f"Error caught for non-numeric input: {e}")
        
    print(f"Area of square with side 10.5: {calculate_square_area(10.5)}")