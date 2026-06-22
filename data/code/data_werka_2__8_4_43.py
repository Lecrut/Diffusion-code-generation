import math

SHAPE_AREAS = {
    'rectangle': lambda dimensions: dimensions[0] * dimensions[1],
    'circle': lambda dimensions: math.pi * dimensions[0] ** 2
}

def calculate_area(shape_type, dimensions):
    if shape_type in SHAPE_AREAS:
        return SHAPE_AREAS[shape_type](dimensions)
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', (10, 5))
    circle_area = calculate_area('circle', (7,))
    print(rectangle_area)
    print(circle_area)