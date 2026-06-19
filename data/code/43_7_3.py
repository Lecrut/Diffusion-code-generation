"""Module to calculate the area of a square."""

def get_square_area(side: float) -> float:
    """Calculate the area of a square given its side length.

    Args:
        side (float): The length of one side of the square, must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side length is negative.
    """
    if side < 0:
        raise ValueError("Side length cannot be negative.")
    return side * side

if __name__ == '__main__':
    sample_side = 5.0
    calculated_area = get_square_area(sample_side)
    print(f"The area of a square with side {sample_side} is {calculated_area}.")