def calculate_square_area(side: float) -> float:
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side * side

if __name__ == '__main__':
    sample_side_length = 5.0
    area = calculate_square_area(sample_side_length)
    print(f"The area of the square with side {sample_side_length} is {area}")