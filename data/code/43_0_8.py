"""
Script to calculate the area of a square given its side length.

This module defines a function to compute the area of a square using the formula: Area = side^2.
It includes a main execution block with hard-coded sample values for demonstration purposes,
requiring no user input or external dependencies.
"""

def calculate_square_area(side_length):
    """
    Calculate the area of a square given its side length.

    Args:
        side_length (float | int): The length of one side of the square. Must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side_length is negative or not a number.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    # Calculate area using standard multiplication (equivalent to exponentiation for power 2)
    return float(side_length * side_length)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # These run without user input, command-line arguments, or network access.

    test_cases = [5.0, 10, -3]

    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f"Side length: {value} -> Area of square: {area}")
        except ValueError as e:
            print(f"Error calculating area for side {value}: {e}")