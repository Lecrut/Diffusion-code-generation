import math
PI = math.pi

def calculate_area(shape, **kwargs):
    area_calculators = {'square': lambda side: side * side, 'circle': lambda radius: PI * radius * radius}
    if shape not in area_calculators:
        raise ValueError(f'Unsupported shape: {shape}')
    calculator_function = area_calculators[shape]
    return calculator_function(**kwargs)
if __name__ == '__main__':
    try:
        side_length = 8
        square_area_result = calculate_area('square', side=side_length)
        radius_length = 5
        circle_area_result = calculate_area('circle', radius=radius_length)
        print(f'Area of square with side {side_length}: {square_area_result}')
        print(f'Area of circle with radius {radius_length}: {circle_area_result}')
    except ValueError as e:
        print(e)