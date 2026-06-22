def calculate_square_area(side_length):
    if side_length <= 0:
        raise ValueError("Side length must be positive")
    return side_length ** 2

if __name__ == '__main__':
    test_cases = {
        'valid': [5, 10],
        'invalid': [-3, 0, "invalid", None]
    }
    
    for category, values in test_cases.items():
        print(f"Testing {category} cases:")
        for value in values:
            try:
                area_value = calculate_square_area(value)
                print(f"Side length: {value}, Area of square: {area_value}")
            except ValueError as e:
                print(f"Error calculating area for side {value}: {e}")