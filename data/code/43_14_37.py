def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError('Side length must be a numeric value.')
    if side_length < 0:
        raise ValueError('Side length cannot be negative.')
    return side_length * side_length

if __name__ == '__main__':
    test_cases = {
        'positive_integer': 5,
        'positive_float': 3.5,
        'negative_number': -2,
        'non_numeric': 'a'
    }
    
    for description, value in test_cases.items():
        try:
            result = calculate_square_area(value)
            print(f"Area of square with {description} side length {value}: {result}")
        except ValueError as e:
            print(f"Error calculating area with {description} side length {value}: {e}")