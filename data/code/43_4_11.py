def calculate_square_area(side):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side (int | float): The length of one side of the square.
        
    Returns:
        int | float: The area of the square.
        
    Raises:
        ValueError: If 'side' is not an integer or float, or if it represents a negative number.
    """
    try:
        # Attempt to convert input to float for validation and calculation
        side_value = float(side)
        
        # Check for non-numeric types that fail conversion (e.g., strings without numbers)
        # If the original type was not numeric, this will raise a ValueError during conversion.
        if isinstance(side, bool):
            raise TypeError("Boolean input is not allowed.")
            
    except (ValueError, TypeError):
        raise ValueError(f"Invalid side length: '{side}' must be a number.") from None
    
    # Ensure the side is non-negative
    if side_value < 0:
        raise ValueError("Side length cannot be negative.")

    return side_value ** 2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    test_cases = [5, "7", -3.5, True]
    
    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f"Side: {value} -> Area: {area}")
        except ValueError as e:
            print(f"Error processing side '{value}': {e}")