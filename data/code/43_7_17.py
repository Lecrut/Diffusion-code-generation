"""Module to calculate the area of a square."""

def calculate_square_area(side_length: float) -> float:
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
    
    return side_length * side_length

if __name__ == '__main__':
    sample_side = 5.0
    
    area_result = calculate_square_area(sample_side)
    print(f"Area of a square with side {sample_side}: {area_result}")