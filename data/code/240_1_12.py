def calculate_square_area(side_length: int) -> int:
    if side_length < 0:
        raise ValueError("Side length must be non-negative.")
    return side_length * side_length

if __name__ == '__main__':
    sample_sides = [5, 10, 3]
    for side in sample_sides:
        area = calculate_square_area(side)
        print(f"The area of a square with side {side} is: {area}")