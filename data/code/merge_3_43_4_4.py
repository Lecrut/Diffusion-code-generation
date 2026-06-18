def calculate_square_area(side):
    """
    Calculates the area of a square given its side length.
    
    Args:
        side (int or float): The length of one side of the square.
        
    Returns:
        int or float: The area of the square.
        
    Raises:
        ValueError: If the input is not numeric (int, float) or cannot be converted to a number.
    """
    try:
        return round(side ** 2, 5) if isinstance(side, (int, float)) else "ValueError"
    
    except TypeError as e:
        raise ValueError(f"The side must be a numeric value. Error encountered: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [5, 3.14, "invalid", None]
    
    print("Testing calculate_square_area function:\n")
    
    for side in test_cases:
        try:
            area_result = calculate_square_area(side)
            
            if isinstance(area_result, str):
                # Handle non-numeric input where the error is returned as a string or raised earlier
                pass
            
            print(f"Side length: {side}")
            print(f"Calculated Area: {area_result}")
            print("-" * 20)
            
        except ValueError as ve:
            print(f"Input: {side}")
            print(f"Error (ValueError): {ve}")
            print("-" * 20)