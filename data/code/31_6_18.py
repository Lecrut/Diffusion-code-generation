def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    return side_length ** 2

if __name__ == '__main__':
    print(calculate_square_area(5))
    print(calculate_square_area(0))
    try:
        print(calculate_square_area(-3))
    except ValueError as e:
        print(str(e))