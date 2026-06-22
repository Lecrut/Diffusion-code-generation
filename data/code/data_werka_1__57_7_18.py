import math
PI = math.pi

def calculate_area(shape_type, dimensions):
    if shape_type.lower() == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape_type.lower() == 'circle':
        radius = dimensions[0]
        return PI * radius ** 2
    else:
        raise ValueError('Unsupported shape type')
if __name__ == '__main__':
    rectangle_dimensions = (5, 3)
    circle_dimensions = (4,)
    rectangle_area = calculate_area('rectangle', rectangle_dimensions)
    circle_area = calculate_area('circle', circle_dimensions)
    print(f'Rectangle area with dimensions {rectangle_dimensions}: {rectangle_area}')
    print(f'Circle area with radius {circle_dimensions[0]}: {circle_area}')