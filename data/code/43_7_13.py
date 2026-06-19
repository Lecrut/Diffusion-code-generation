import math

def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length.

    Args:
        side_length (float): The length of one side of the square, must be non-negative.

    Returns:
        float: The calculated area of the square.

    Raises:
        ValueError: If the side length is negative.
    """
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    
    return side_length ** 2

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample_sides = [5, -3.5, 10]

    print(f"Area of square with side length {sample_sides[0]}: {calculate_square_area(sample_sides[0])}")
    
    try:
        result_negative = calculate_square_area(-3.5)
    except ValueError as e:
        print(f"Error for negative input: {e}")

    print(f"Area of square with side length {sample_sides[-1]}: {calculate_square_area(sample_sides[-1])}")