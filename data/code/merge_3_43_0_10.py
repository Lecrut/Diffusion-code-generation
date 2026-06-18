"""
Script to calculate the area of a square given its side length.

This module defines a function to compute the area using the formula: Area = side * side.
It includes a main execution block with hard-coded sample values that run without user input.
"""

def calculate_square_area(side_length):
    """
    Calculate the area of a square based on its side length.

    Args:
        side_length (float or int): The length of one side of the square. Must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side_length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [5, 10.5, -3]

    print("--- Square Area Calculator ---\n")
    
    for value in test_cases:
        try:
            area = calculate_square_area(value)
            side_repr = f"{value}" if isinstance(value, int) else str(value)
            print(f"Side Length ({side_repr}): {area}")
            
            # Note: The case of -3 is included to demonstrate error handling logic.
        except ValueError as e:
            print(f"Illegal Input for Side Length {value}: {e}")

    print("--- Execution Complete ---")