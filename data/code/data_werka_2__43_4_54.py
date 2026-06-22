def calculate_square_area(side_length: float) -> float:
    if side_length < 0:
        raise ValueError('Side length cannot be negative')
    area_calculation_methods = {'default': lambda x: x ** 2}
    method_key = 'default'
    return area_calculation_methods[method_key](side_length)
if __name__ == '__main__':
    sample_side_length = 4.0
    area = calculate_square_area(sample_side_length)
    print(area)