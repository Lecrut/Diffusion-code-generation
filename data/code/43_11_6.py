def calculate_square_area(side_length: float) -> float:
    """
    Calculates the area of a square given its side length.

    Args:
        side_length (float): The length of one side of the square. Must be non-negative.

    Returns:
        float: The calculated area.

    Raises:
        ValueError: If the provided side_length is negative.

    Example:
        >>> calculate_square_area(5)
        25.0
    """
    if side_length < 0:
        raise ValueError("Side length must be non-negative.")
    
    return float(side_length * side_length)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [3.5, -2, 10]

    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f"Area of a square with side length {value}: {area}")
        except ValueError as e:
            print(f"Error calculating area for {value}: {e}")