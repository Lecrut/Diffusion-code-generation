"""Module to calculate the area of a square."""

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length.

    Args:
        side_length (float): The length of one side of the square. Must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_side = 5.0
    
    area_result = calculate_square_area(test_side)
    print(f"The area of a square with side length {test_side} is {area_result}")

    # Additional test case to demonstrate functionality further.
    test_side_2 = 10.5
    area_result_2 = calculate_square_area(test_side_2)
    print(f"The area of a square with side length {test_side_2} is {area_result_2}")