def is_numeric(value):
    return isinstance(value, (int, float))

def is_non_negative(value):
    return value >= 0

def calculate_square_area(side_length):
    if not is_numeric(side_length):
        raise ValueError('Side length must be a numeric value.')
    if not is_non_negative(side_length):
        raise ValueError('Side length cannot be negative.')
    return side_length * side_length

if __name__ == '__main__':
    test_values = [10, 2.5, -1, 'test', 0]
    for value in test_values:
        try:
            area = calculate_square_area(value)
            print(f"Area of square with side {value}: {area}")
        except ValueError as e:
            print(e)