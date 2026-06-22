import math
PI = math.pi

def calculate_area(shape, **kwargs):
    area_calculators = {'square': lambda side: side * side, 'circle': lambda radius: PI * radius * radius}
    if shape in area_calculators:
        return area_calculators[shape](**kwargs)
    else:
        raise ValueError(f'Unsupported shape: {shape}')
if __name__ == '__main__':
    square_side = 4.5
    circle_radius = 2.0
    square_area = calculate_area('square', side=square_side)
    circle_area = calculate_area('circle', radius=circle_radius)
    print(f'Area of square with side {square_side}: {square_area}')
    print(f'Area of circle with radius {circle_radius}: {circle_area}')