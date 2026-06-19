import math
SHAPE_SQUARE = 'square'
SHAPE_CIRCLE = 'circle'

def calculate_area(shape, **kwargs):
    area_calculators = {SHAPE_SQUARE: lambda side: side * side, SHAPE_CIRCLE: lambda radius: math.pi * radius * radius}
    if shape in area_calculators:
        return area_calculators[shape](**kwargs)
    else:
        raise ValueError(f'Unsupported shape: {shape}')
if __name__ == '__main__':
    square_side = 6
    circle_radius = 4
    square_area = calculate_area(SHAPE_SQUARE, side=square_side)
    circle_area = calculate_area(SHAPE_CIRCLE, radius=circle_radius)
    print(f'Area of square with side {square_side}: {square_area}')
    print(f'Area of circle with radius {circle_radius}: {circle_area}')