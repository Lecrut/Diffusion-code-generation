import math

def calculate_area(shape_type, **kwargs):
    if shape_type == 'rectangle':
        width = kwargs.get('width')
        height = kwargs.get('height')
        if width is None or height is None:
            raise ValueError('Rectangle requires both width and height')
        return width * height
    elif shape_type == 'circle':
        radius = kwargs.get('radius')
        if radius is None:
            raise ValueError('Circle requires a radius')
        return math.pi * radius ** 2
    elif shape_type == 'triangle':
        base = kwargs.get('base')
        height = kwargs.get('height')
        if base is None or height is None:
            raise ValueError('Triangle requires both base and height')
        return 0.5 * base * height
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')
if __name__ == '__main__':
    try:
        print(calculate_area('rectangle', width=5, height=10))
        print(calculate_area('circle', radius=7))
        print(calculate_area('triangle', base=6, height=4))
        print(calculate_area('square', side=5))
    except ValueError as e:
        print(e)