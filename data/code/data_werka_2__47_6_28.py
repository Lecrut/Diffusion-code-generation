def calculate_area(shape):
    return {
        'rectangle': lambda s: s['length'] * s['width'],
        'circle': lambda s: 3.14159 * s['radius'] ** 2,
        'triangle': lambda s: 0.5 * s['base'] * s['height']
    }.get(shape['type'], lambda _: 0)(shape)

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'length': 5, 'width': 3},
        {'type': 'circle', 'radius': 4},
        {'type': 'triangle', 'base': 6, 'height': 2}
    ]
    for shape in shapes:
        print(calculate_area(shape))