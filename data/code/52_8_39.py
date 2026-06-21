import math
SHAPE_AREA_FUNCTIONS = {'rectangle': lambda width, height: width * height, 'circle': lambda radius: math.pi * radius ** 2, 'triangle': lambda base, height: 0.5 * base * height}

def calculate_area(shape_type, *args):
    if shape_type not in SHAPE_AREA_FUNCTIONS:
        raise ValueError(f'Unsupported shape type: {shape_type}')
    area_function = SHAPE_AREA_FUNCTIONS[shape_type]
    if len(args) != area_function.__code__.co_argcount:
        raise ValueError(f'Shape {shape_type} requires {area_function.__code__.co_argcount} parameters')
    return area_function(*args)
if __name__ == '__main__':
    print(calculate_area('rectangle', 5, 10))
    print(calculate_area('circle', 7))
    print(calculate_area('triangle', 8, 6))