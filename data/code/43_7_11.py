from typing import Union

def calculate_square_area(side: float) -> float:
    """Calculate the area of a square given its side length.

    Args:
        side (float): The length of one side of the square, must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side is negative or not a number.
    """
    if not isinstance(side, (int, float)):
        raise TypeError("Side length must be an integer or float.")
    
    if side < 0:
        raise ValueError("Side length cannot be negative.")

    return side ** 2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print(calculate_square_area(5))   # Output: 25.0
    print(calculate_square_area(-3)) # Raises ValueError