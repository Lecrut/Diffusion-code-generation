def calculate_square_area(side_length):
    side_type = type(side_length)
    valid_types = {int, float}
    if side_type not in valid_types:
        raise ValueError('Side length must be a numeric value.')
    if side_length < 0:
        raise ValueError('Side length cannot be negative.')
    return side_length * side_length

if __name__ == '__main__':
    sample_values = [10, 2.5, -1, 'test']
    results = {}
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            results[value] = area
        except ValueError as e:
            results[value] = str(e)
    
    for value, result in results.items():
        print(f"Area of square with side {value}: {result}")