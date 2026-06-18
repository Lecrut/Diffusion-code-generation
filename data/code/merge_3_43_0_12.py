"""
Script to calculate the area of a square given its side length.

This module defines a function to compute the area of a square using 
the formula: Area = side * side (or side^2). It includes basic input validation 
to ensure the side length is non-negative and numeric. The main execution block 
demonstrates usage with hard-coded sample values, requiring no user interaction or external dependencies.
"""

def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.

    Parameters:
        side_length (float | int): The length of one side of the square. Must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        TypeError: If side_length is not a number.
        ValueError: If side_length is negative.
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be an integer or float.")
    
    if side_length < 0:
        raise ValueError("side_length cannot be negative.")

    return side_length ** 2

if __name__ == '__main__':
    # Sample values for demonstration. No user input is required.
    sample_side = 5
    
    try:
        area = calculate_square_area(sample_side)
        print(f"The area of a square with side length {sample_side} is {area}.")
    except (TypeError, ValueError) as e:
        print(f"Error calculating area: {e}")