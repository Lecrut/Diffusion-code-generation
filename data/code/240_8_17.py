def calculate_square_area(side):
    if side < 0:
        raise ValueError('Side length must be non-negative')
    return side * side
if __name__ == '__main__':
    print(calculate_square_area(5))
    print(calculate_square_area(0))
    try:
        print(calculate_square_area(-1))
    except ValueError as e:
        print(e)