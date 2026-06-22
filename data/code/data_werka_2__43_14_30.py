def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError('Side length must be a numeric value.')
    if side_length < 0:
        raise ValueError('Side length cannot be negative.')
    return side_length ** 2

if __name__ == '__main__':
    test_values = [10, 7.5, -1, 'invalid']
    for value in test_values:
        try:
            area = calculate_square_area(value)
            print(f"The area of a square with side length {value} is: {area}")
        except ValueError as e:
            print(e)