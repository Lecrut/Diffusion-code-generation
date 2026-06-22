def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError('Side length must be a numeric value.')
    if side_length < 0:
        raise ValueError('Side length cannot be negative.')

def calculate_square_area(side_length):
    validate_side_length(side_length)
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [10, 2.3, -1, 'abc']
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            print(f"Area of square with side {value}: {area}")
        except ValueError as e:
            print(e)