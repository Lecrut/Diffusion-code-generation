MINIMUM_SIDE_LENGTH = 0

def calculate_square_area(side_length):
    if side_length <= MINIMUM_SIDE_LENGTH:
        raise ValueError('Side length must be positive')
    return side_length ** 2

if __name__ == '__main__':
    try:
        print(calculate_square_area(6))
        print(calculate_square_area(-5))
    except ValueError as e:
        print(e)