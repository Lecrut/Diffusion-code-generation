import math

def calculate_square_area(side):
    """Calculates the area of a square given its side length.
    
    Args:
        side (int | float): The length of one side of the square.
        
    Returns:
        int or float: The calculated area of the square.
        
    Raises:
        ValueError: If 'side' is not a numeric type.
    """
    if not isinstance(side, (int, float)):
        raise ValueError(f"Input must be a number, got {type(side).__name__}")
    
    return side * side

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    try:
        area_1 = calculate_square_area(5)
        print(f"Area of square with side 5: {area_1}")
        
        area_2 = calculate_square_area(3.5)
        print(f"Area of square with side 3.5: {area_2}")
        
    except ValueError as e:
        print(f"Error occurred: {e}")