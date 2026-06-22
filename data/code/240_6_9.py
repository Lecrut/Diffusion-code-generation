def calculate_square_area(side):
    if side < 0:
        raise ValueError("Side length must be non-negative")
    return side * side

if __name__ == '__main__':
    try:
        sample_side = 5.0
        area = calculate_square_area(sample_side)
        print(f"The side of the square is: {sample_side}")
        print(f"The area of the square is: {area}")
    except ValueError as e:
        print(e)