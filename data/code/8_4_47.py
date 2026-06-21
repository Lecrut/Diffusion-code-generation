import math
PI = math.pi

def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape_type == 'circle':
        radius = dimensions[0]
        return PI * radius * radius
    else:
        raise ValueError('Unsupported shape type')
if __name__ == '__main__':
    rectangle_dimensions = (10, 5)
    circle_dimensions = (3,)
    rectangle_area = calculate_area('rectangle', rectangle_dimensions)
    circle_area = calculate_area('circle', circle_dimensions)
    print(rectangle_area)
    print(circle_area)