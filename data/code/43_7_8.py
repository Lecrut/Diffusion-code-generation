"""Module to calculate the area of a square."""

def get_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length.

    Args:
        side_length (float): The length of one side of the square. Must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If side_length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [5, -3.5, 10]

    for case in test_cases:
        try:
            area = get_square_area(case)
            print(f"Area of square with side {case}: {area}")
        except ValueError as error:
            print(f"Error calculating area for side {case}: {error}")