def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError('Side length must be a numeric value.')
    if side_length < 0:
        return 'Error: Side length cannot be negative.'
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [4, 6.2, -3, 'a']
    for value in sample_values:
        try:
            result = calculate_square_area(value)
            print(f"Area of square with side {value}: {result}")
        except ValueError as e:
            print(e)