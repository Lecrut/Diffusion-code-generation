def calculate_area(shape):
    match shape['type']:
        case 'rectangle':
            return shape['length'] * shape['width']
        case 'circle':
            return 3.14159 * shape['radius'] ** 2
        case 'triangle':
            return 0.5 * shape['base'] * shape['height']
        case _:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'length': 5, 'width': 3},
        {'type': 'circle', 'radius': 4},
        {'type': 'triangle', 'base': 6, 'height': 2}
    ]
    for shape in shapes:
        print(calculate_area(shape))