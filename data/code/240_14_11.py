def calculate_area(side_length):
    if not isinstance(side_length, (int, float)) or side_length < 0:
        raise ValueError('Side length must be a non-negative number')
    return float(side_length ** 2)
if __name__ == '__main__':
    try:
        print(calculate_area(5))
        print(calculate_area(3.14))
        print(calculate_area(-1))
    except ValueError as e:
        print(e)