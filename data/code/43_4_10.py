def calculate_square_area(side):
    """Calculates the area of a square given its side length."""
    try:
        side = float(side)
        if side < 0:
            raise ValueError("Side length must be non-negative.")
        return side * side
    except TypeError as e:
        raise ValueError(f"Invalid input type. Expected numeric, got {type(side).__name__}.") from e

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user interaction
    samples = [5, "4", 3.14, -2]

    for side in samples:
        try:
            area = calculate_square_area(side)
            print(f"Side {side}: Area is {area}")
        except ValueError as e:
            print(f"Error calculating area for {side}: {e}")