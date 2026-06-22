def calculate_square_area(side_length):
    if side_length <= 0:
        raise ValueError('Side length must be positive')
    return side_length ** 2

if __name__ == '__main__':
    try:
        sample_values = {
            'positive': 6,
            'negative': -5,
            'zero': 0
        }
        
        for description, value in sample_values.items():
            print(f"Calculating area for {description} side length ({value}):")
            try:
                area = calculate_square_area(value)
                print(f"Area: {area}")
            except ValueError as e:
                print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")