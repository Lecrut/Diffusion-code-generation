import math

def calculate_area(shape_type, **kwargs):
    if shape_type == 'rectangle':
        length = kwargs.get('length')
        width = kwargs.get('width')
        if length is None or width is None:
            raise ValueError('Missing required parameters for rectangle: length and width')
        return length * width
    elif shape_type == 'circle':
        radius = kwargs.get('radius')
        if radius is None:
            raise ValueError('Missing required parameter for circle: radius')
        return math.pi * radius ** 2
    elif shape_type == 'triangle':
        base = kwargs.get('base')
        height = kwargs.get('height')
        if base is None or height is None:
            raise ValueError('Missing required parameters for triangle: base and height')
        return 0.5 * base * height
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')
if __name__ == '__main__':
    try:
        print(calculate_area('rectangle', length=5, width=3))
        print(calculate_area('circle', radius=4))
        print(calculate_area('triangle', base=6, height=4))
        print(calculate_area('square', side=4))
    except ValueError as e:
        print(e)