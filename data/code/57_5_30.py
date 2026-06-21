import math
PI = math.pi

def calculate_area(shape, **kwargs):
    area_calculators = {'square': lambda side: side * side, 'circle': lambda radius: PI * radius * radius}
    if shape not in area_calculators:
        raise ValueError(f'Unsupported shape: {shape}')
    return area_calculators[shape](**kwargs)
if __name__ == '__main__':
    try:
        square_side = 5
        circle_radius = 3
        square_area_result = calculate_area('square', side=square_side)
        circle_area_result = calculate_area('circle', radius=circle_radius)
        print(f'Area of square with side {square_side}: {square_area_result}')
        print(f'Area of circle with radius {circle_radius}: {circle_area_result}')
    except ValueError as e:
        print(e)