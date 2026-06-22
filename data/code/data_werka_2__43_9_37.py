def calculate_square_area(side_length):
    if side_length <= 0:
        raise ValueError('Side length must be positive')
    return side_length ** 2

if __name__ == '__main__':
    try:
        print(calculate_square_area(7))
        print(calculate_square_area(-2))
    except ValueError as e:
        print(e)