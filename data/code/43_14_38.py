def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError('Side length must be a numeric value.')
    if side_length < 0:
        raise ValueError('Side length cannot be negative.')
    return side_length ** 2

if __name__ == '__main__':
    try:
        print(calculate_square_area(10))
        print(calculate_square_area(2.3))
        print(calculate_square_area(-1))
        print(calculate_square_area('a'))
    except ValueError as e:
        print(e)