"""Module to calculate the area of a square."""

def square_area(side: float) -> float:
    """Calculate the area of a square given its side length.

    Args:
        side (float): The length of one side of the square, must be positive.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side is not greater than zero.
    """
    if side <= 0:
        raise ValueError("Side length must be greater than zero.")
    
    return side ** 2

if __name__ == '__main__':
    sample_sides = [5, -3, 1]
    for value in sample_sides:
        try:
            area = square_area(value)
            print(f"Area of a square with side {value}: {area}")
        except ValueError as e:
            print(f"Error calculating area for side {value}: {e}")