def calculate_area(shape):
    areas = {
        'rectangle': lambda l, w: l * w,
        'circle': lambda r: 3.14159 * r**2,
        'triangle': lambda b, h: 0.5 * b * h
    }
    return areas.get(shape['type'], lambda *_: None)(*shape.values())

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'length': 5, 'width': 3},
        {'type': 'circle', 'radius': 4},
        {'type': 'triangle', 'base': 6, 'height': 2}
    ]
    for shape in shapes:
        print(calculate_area(shape))