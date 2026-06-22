import math
SHAPE_SQUARE = 'square'
SHAPE_CIRCLE = 'circle'
area_calculators = {SHAPE_SQUARE: lambda side: side * side, SHAPE_CIRCLE: lambda radius: math.pi * radius * radius}

def calculate_area(shape, **kwargs):
    if shape in area_calculators:
        return area_calculators[shape](**kwargs)
    else:
        raise ValueError(f'Unsupported shape: {shape}')
if __name__ == '__main__':
    square_side = 7.0
    circle_radius = 4.5
    square_area = calculate_area(SHAPE_SQUARE, side=square_side)
    circle_area = calculate_area(SHAPE_CIRCLE, radius=circle_radius)
    print(f'Area of square with side {square_side}: {square_area}')
    print(f'Area of circle with radius {circle_radius}: {circle_area}')