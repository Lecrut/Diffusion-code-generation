"""Module to calculate the area of a square."""

def get_square_area(side: float) -> float:
    """Calculate the area of a given square side length.

    Args:
        side (float): The length of one side of the square, must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side is negative or not numeric.
    """
    if isinstance(side, (int, float)) and side < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side * side

if __name__ == '__main__':
    # Sample values for testing without user input
    test_cases = [5.0, -3, "10", 0]

    for value in test_cases:
        try:
            area = get_square_area(value)
            print(f"Area of square with side {value}: {area}")
        except ValueError as e:
            print(f"Error calculating area for input {value}: {e}")