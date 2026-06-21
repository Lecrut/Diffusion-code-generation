def calculate_square_area(side_length):
    if side_length <= 0:
        raise ValueError('Side length must be positive')
    return side_length ** 2

if __name__ == '__main__':
    try:
        sample_values = [4, -5, 6]
        for value in sample_values:
            print(calculate_square_area(value))
    except ValueError as e:
        print(e)