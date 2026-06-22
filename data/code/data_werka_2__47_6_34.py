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
        {'type': 'rectangle', 'length': 5, 'width': 3},
        {'type': 'circle', 'radius': 4},
        {'type': 'triangle', 'base': 6, 'height': 2}
    ]
    for shape in shapes:
        print(calculate_area(shape))