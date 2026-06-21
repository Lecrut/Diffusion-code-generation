def calculate_square_area(side_length):
    side_length_type = type(side_length)
    valid_types = (int, float)
    
    if side_length_type not in valid_types:
        raise ValueError('Side length must be a numeric value.')
    
    if side_length < 0:
        raise ValueError('Side length cannot be negative.')
    
    return side_length * side_length

if __name__ == '__main__':
    test_values = {
        'positive_int': 5,
        'positive_float': 3.5,
        'negative_value': -2,
        'non_numeric': 'a'
    }
    
    for label, value in test_values.items():
        try:
            area = calculate_square_area(value)
            print(f"Area of square with {label} side length {value}: {area}")
        except ValueError as e:
            print(f"Error calculating area for {label} side length {value}: {e}")