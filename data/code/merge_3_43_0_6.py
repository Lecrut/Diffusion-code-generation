"""
Module to calculate the area of a square given its side length.

This script defines a function to compute the area using the formula: Area = side * side.
It includes basic input validation and an interactive block with hard-coded sample values 
for demonstration purposes, ensuring no external inputs or network access are required.
"""

def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.

    Args:
        side_length (float): The length of one side of the square. Must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side length is negative or not numeric.
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("Side length must be a number.")
    
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")

    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for demonstration.
    # No user input, command-line arguments, or network access is used here.
    
    samples = [5.0, 10, -3]
    
    print("Testing calculate_square_area function with hard-coded samples:\n")
    
    for side in samples:
        try:
            area = calculate_square_area(side)
            if isinstance(area, float):
                formatted_side = f"{side:.2f}"
                formatted_area = f"{area:.2f}"
                print(f"Side length ({formatted_side}): Area is {formatted_area}")
            else:
                print(f"Side length ({side}): Area is {area}")
        except (ValueError, TypeError) as e:
            print(f"Error for side length {side}: {e}")