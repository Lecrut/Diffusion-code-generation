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
        raise ValueError("Side length must be non-negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing the function without user input.
    side_a = 5.0
    area_a = get_square_area(side_a)

    side_b = -3.0
    try:
        area_b = get_square_area(side_b)
    except ValueError as e:
        print(f"Error for negative side length {side_b}: {e}")

    # Print results to console
    print(f"Area of square with side {side_a} is {area_a}.")