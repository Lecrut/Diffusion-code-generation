def validate_shape(shape):
    if shape not in ['rectangle', 'circle', 'triangle']:
        raise ValueError("Unsupported shape")

def calculate_area(shape, **kwargs):
    validate_shape(shape)
    return {
        'rectangle': lambda l, w: l * w,
        'circle': lambda r: 3.14159 * r**2,
        'triangle': lambda b, h: 0.5 * b * h
    }[shape](**kwargs)

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'length': 5, 'width': 3},
        {'type': 'circle', 'radius': 4},
        {'type': 'triangle', 'base': 6, 'height': 2}
    ]
    for shape in shapes:
        print(calculate_area(shape['type'], **{k: v for k, v in shape.items() if k != 'type'}))