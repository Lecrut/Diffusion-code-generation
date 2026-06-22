import math

def calculate_area(shape_params):
    shape_type = shape_params.get('type')
    if shape_type == 'circle':
        radius = shape_params.get('radius')
        if radius is None or radius <= 0:
            raise ValueError("Circle requires a positive radius")
        return math.pi * (radius ** 2)
    elif shape_type == 'rectangle':
        width = shape_params.get('width')
        height = shape_params.get('height')
        if width is None or height is None or width <= 0 or height <= 0:
            raise ValueError("Rectangle requires positive width and height")
        return width * height
    elif shape_type == 'triangle':
        base = shape_params.get('base')
        height = shape_params.get('height')
        if base is None or height is None or base <= 0 or height <= 0:
            raise ValueError("Triangle requires positive base and height")
        return 0.5 * base * height
    elif shape_type == 'square':
        side = shape_params.get('side')
        if side is None or side <= 0:
            raise ValueError("Square requires a positive side length")
        return side ** 2
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    circle_params = {'type': 'circle', 'radius': 5}
    print(calculate_area(circle_params))

    rect_params = {'type': 'rectangle', 'width': 4, 'height': 6}
    print(calculate_area(rect_params))

    triangle_params = {'type': 'triangle', 'base': 10, 'height': 3}
    print(calculate_area(triangle_params))

    square_params = {'type': 'square', 'side': 7}
    print(calculate_area(square_params))