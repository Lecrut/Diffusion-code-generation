import math

def calculate_square_area(side_length: float) -> float:
    """
    Calculate the area of a square given its side length.
    
    The formula used is Area = side * side.
    
    Args:
        side_length (float): A positive number representing the length of one side of the square.
        
    Returns:
        float: The calculated area of the square.
        
    Raises:
        ValueError: If the side_length is negative or zero.
    """
    if side_length < 0:
        raise ValueError("Side length must be a positive number.")
    
    return math.sqrt(side_length) ** 2

if __name__ == '__main__':
    # Sample test cases run without user input, command-line arguments, or network access.
    sample_sides = [5.0, 3.14, -2]  # Including a negative value to demonstrate error handling
    
    for side in sample_sides:
        try:
            area = calculate_square_area(side)
            print(f"Side length: {side}, Area: {area}")
        except ValueError as e:
            print(f"Error for input {side}: {e}")