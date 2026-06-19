def calculate_square_area(side_length):
    """
    Calculates the area of a square given its side length.

    Args:
        side_length (float or int): The length of one side of the square.

    Returns:
        float: The calculated area of the square.
    
    Raises:
        TypeError: If the input is not a number.
        ValueError: If the input is negative.
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be a numerical value.")
    if side_length < 0:
        raise ValueError("side_length cannot be negative.")

    return side_length * side_length

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [5, -3.5, "invalid", 10]

    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f"Area of square with side {value}: {area}")
        except (TypeError, ValueError) as e:
            print(f"Error calculating area for {value}: {e}")