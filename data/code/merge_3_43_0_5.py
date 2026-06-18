"""
Script to calculate the area of a square given its side length.

This module defines a function to compute the area of a square using 
the formula: Area = side * side. It includes a main execution block 
with hard-coded sample values for demonstration purposes, ensuring no 
user input or external dependencies are required.
"""

def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.

    Args:
        side_length (float | int): The length of one side of the square. Must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side_length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments.
    SAMPLE_SIDES = [5, -3, 10.5]

    print("Calculating areas of squares with the following side lengths:")
    
    for side in SAMPLE_SIDES:
        try:
            area = calculate_square_area(side)
            print(f"Side length {side}: Area is {area}")
        except ValueError as e:
            print(f"Error calculating area for side {side}: {e}")