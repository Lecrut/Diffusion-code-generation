"""Module to calculate the area of a square."""

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length.

    Args:
        side_length (float): The length of one side of the square. Must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If side_length is negative.
    
    Example:
        >>> calculate_square_area(5)
        25.0
    
    """
    if side_length < 0:
        raise ValueError("Side length must be non-negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [5, -3, 0]

    print(f'Calculating area of a square with side length: {test_cases[0]}')
    result_1 = calculate_square_area(test_cases[0])
    print(f'Result: {result_1}')

    try:
        result_2 = calculate_square_area(test_cases[1])
    except ValueError as e:
        print(f'Error for negative side length ({test_cases[1]}): {e}')

    result_3 = calculate_square_area(test_cases[2])
    print(f'Result for zero side length: {result_3}')