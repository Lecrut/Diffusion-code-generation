def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side_length (numeric type or convertible to numeric): The length of one side of the square.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If 'side_length' cannot be converted to a number.
    """
    try:
        # Attempt to convert input to float for calculation and validation
        numeric_side = float(side_length)
        return numeric_side * numeric_side
    except TypeError as e:
        raise ValueError("Input must be convertible to a numeric value.") from e

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Valid integer side length
    valid_int = 5
    
    # Valid float side length
    valid_float = 2.5
    
    print(f"Area of square with side {valid_int}:")
    try:
        area1 = calculate_square_area(valid_int)
        print(area1)
    except ValueError as ve:
        print(f"Error for integer input: {ve}")

    print(f"\nArea of square with side {valid_float}:")
    try:
        area2 = calculate_square_area(valid_float)
        print(area2)
    except ValueError as ve:
        print(f"Error for float input: {ve}")

    # Invalid string input to demonstrate error handling
    invalid_input = "not a number"