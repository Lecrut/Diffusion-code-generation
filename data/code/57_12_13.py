import math

SHAPE_AREA_FUNCTIONS = {
    'circle': lambda r: math.pi * r ** 2,
}

def calculate_area(shape_type, dimensions):
    if shape_type in SHAPE_AREA_FUNCTIONS:
        return SHAPE_AREA_FUNCTIONS[shape_type](*dimensions)
    else:
        raise ValueError("Invalid shape type")

if __name__ == '__main__':
    radius = 5
    circle_area = calculate_area('circle', (radius,))
    print(circle_area)