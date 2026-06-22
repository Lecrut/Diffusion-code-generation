def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError('Side length must be a non-negative number')
    return side_length * side_length
if __name__ == '__main__':
    try:
        print(calculate_square_area(5))
        print(calculate_square_area(0))
        print(calculate_square_area(100))
        print(calculate_square_area(-1))
    except ValueError as e:
        print(e)