def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise TypeError('Side length must be a number.')
    if side_length <= 0:
        raise ValueError('Side length must be positive.')

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length * side_length
if __name__ == '__main__':
    test_cases = [4, 7.5, -3, 'invalid', None]
    for value in test_cases:
        try:
            area = calculate_square_area(value)
            print(f'Square with side length {value} has an area of {area}.')
        except Exception as e:
            print(f'Error calculating area for side {value}: {e}')