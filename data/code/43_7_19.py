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
    # Hard-coded sample values for testing and demonstration.
    test_cases = [5, -3, 10]

    print(f"Square with side {test_cases[0]}: Area is {get_square_area(test_cases[0])}")
    
    try:
        result = get_square_area(test_cases[1])
        print(f"Square with side {result}: Result should not be printed here.")
    except ValueError as e:
        print(e)

    print(f"Square with side {test_cases[2]}: Area is {get_square_area(test_cases[2])}")