def calculate_square_area(side):
    if not isinstance(side, (int, float)) or side < 0:
        raise ValueError('Side length must be a non-negative number')
    return side * side
if __name__ == '__main__':
    try:
        print(calculate_square_area(5))
        print(calculate_square_area(0))
        print(calculate_square_area(2.5))
        print(calculate_square_area(-1))
    except ValueError as e:
        print(e)