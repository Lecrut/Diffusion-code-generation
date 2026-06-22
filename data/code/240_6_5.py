def calculate_square_area(side):
    if not isinstance(side, (int, float)) or side < 0:
        raise ValueError("Side length must be a non-negative number.")
    return side * side

if __name__ == '__main__':
    sample_side = 5.0
    area = calculate_square_area(sample_side)
    print(f"The side of the square is: {sample_side}")
    print(f"The area of the square is: {area}")