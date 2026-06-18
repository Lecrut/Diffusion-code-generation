import math

def calculate_square_area(side_length: float) -> float:
    """
    Calculates the area of a square given its side length.
    
    Args:
        side_length (float): The length of one side of the square. Must be non-negative.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return math.pow(side_length, 2)

if __name__ == '__main__':
    # Sample values hard-coded for testing without user input or network access
    sample_side_1 = 5.0
    sample_side_2 = -3
    
    print(f"Area of square with side {sample_side_1}: {calculate_square_area(sample_side_1)}")
    
    try:
        result_negative = calculate_square_area(sample_side_2)
    except ValueError as e:
        print(f"Error for negative input {sample_side_2}: {e}")