def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError('Side length must be a numeric value.')
    if side_length < 0:
        return 'Error: Side length cannot be negative.'
    area = side_length * side_length
    return area

if __name__ == '__main__':
    test_cases = {
        'positive_integer': 10,
        'positive_float': 7.5,
        'negative_number': -3,
        'non_numeric': 'a'
    }
    
    for description, value in test_cases.items():
        try:
            result = calculate_square_area(value)
            print(f"{description.capitalize()}: Area of square with side {value}: {result}")
        except ValueError as e:
            print(f"{description.capitalize()}: {e}")