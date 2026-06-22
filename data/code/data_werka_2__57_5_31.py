import math

def calculate_area(shape, **kwargs):
    area_calculators = {'square': lambda side: side * side, 'circle': lambda radius: math.pi * radius * radius}
    if shape not in area_calculators:
        raise ValueError(f'Unsupported shape: {shape}')
    calculator_function = area_calculators[shape]
    return calculator_function(**kwargs)
if __name__ == '__main__':
    try:
        square_side_length = 8
        circle_radius_length = 2.5
        square_area_result = calculate_area('square', side=square_side_length)
        circle_area_result = calculate_area('circle', radius=circle_radius_length)
        print(f'Area of square with side {square_side_length}: {square_area_result}')
        print(f'Area of circle with radius {circle_radius_length}: {circle_area_result}')
    except ValueError as e:
        print(e)