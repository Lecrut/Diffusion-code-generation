def calculate_area(shape):
    area_functions = {
        'rectangle': lambda l, w: l * w,
        'circle': lambda r: 3.14159 * r**2,
        'triangle': lambda b, h: 0.5 * b * h
    }
    try:
        return area_functions[shape['type']](*shape.values())
    except KeyError:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'length': 7, 'width': 2},
        {'type': 'circle', 'radius': 3},
        {'type': 'triangle', 'base': 8, 'height': 5}
    ]
    for shape in shapes:
        print(calculate_area(shape))