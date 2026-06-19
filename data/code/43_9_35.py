def calculate_square_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return side_length ** 2

if __name__ == '__main__':
    try:
        side = -3.0
        area = calculate_square_area(side)
        print(f"Area of square with side {side}: {area}")
    except ValueError as e:
        print(e)