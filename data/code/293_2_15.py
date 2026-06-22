import math
PI = 3.141592653589793
SQUARE_AREA_FACTOR = 1
RECTANGLE_AREA_FACTOR = 1
CIRCLE_AREA_FACTOR = PI / 4

def calculate_area(shape_type, *dimensions):
    if shape_type == 'circle':
        radius = dimensions[0]
        return CIRCLE_AREA_FACTOR * radius ** 2
    elif shape_type == 'square':
        side_length = dimensions[0]
        return SQUARE_AREA_FACTOR * side_length ** 2
    elif shape_type == 'rectangle':
        length, width = dimensions
        return RECTANGLE_AREA_FACTOR * length * width
    else:
        raise ValueError('Unsupported shape type')
if __name__ == '__main__':
    circle_area = calculate_area('circle', 5)
    square_area = calculate_area('square', 3)
    rectangle_area = calculate_area('rectangle', 4, 6)
    print(f'Circle area: {circle_area}')
    print(f'Square area: {square_area}')
    print(f'Rectangle area: {rectangle_area}')