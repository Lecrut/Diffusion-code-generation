def calculate_square_area(side_length: float) -> float:
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 5.0
    calculated_area = calculate_square_area(sample_side)
    print(f"The area of a square with side {sample_side} is {calculated_area}")