def calculate_square_area(side_length):
    if side_length <= 0:
        raise ValueError('Side length must be positive')
    return side_length ** 2

if __name__ == '__main__':
    try:
        test_values = {
            'positive': 6,
            'negative': -5,
            'zero': 0
        }
        
        for description, value in test_values.items():
            print(f"Testing {description} input ({value}):")
            print(calculate_square_area(value))
    except ValueError as e:
        print(e)