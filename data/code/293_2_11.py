import math
PI = 3.141592653589793

def calculate_area(shape, **params):
    if shape == 'circle':
        radius = params['radius']
        return PI * radius ** 2
    elif shape == 'square':
        side = params['side']
        return side ** 2
    elif shape == 'rectangle':
        length = params['length']
        width = params['width']
        return length * width
    else:
        raise ValueError('Unsupported shape')
if __name__ == '__main__':
    circle_area = calculate_area('circle', radius=5)
    square_area = calculate_area('square', side=4)
    rectangle_area = calculate_area('rectangle', length=6, width=3)
    print(f'Circle area: {circle_area}')
    print(f'Square area: {square_area}')
    print(f'Rectangle area: {rectangle_area}')