import math

def validate_shape(shape):
    shape_type = shape.get('type')
    if shape_type == 'rectangle':
        width = shape.get('width')
        height = shape.get('height')
        if width is None or height is None:
            raise ValueError("Rectangle requires both width and height")
    elif shape_type == 'circle':
        radius = shape.get('radius')
        if radius is None:
            raise ValueError("Circle requires a radius")
    elif shape_type == 'triangle':
        base = shape.get('base')
        height = shape.get('height')
        if base is None or height is None:
            raise ValueError("Triangle requires both base and height")
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

def calculate_area(shape):
    validate_shape(shape)
    shape_type = shape['type']
    if shape_type == 'rectangle':
        return shape['width'] * shape['height']
    elif shape_type == 'circle':
        return math.pi * (shape['radius'] ** 2)
    elif shape_type == 'triangle':
        return 0.5 * shape['base'] * shape['height']

if __name__ == '__main__':
    rectangle = {'type': 'rectangle', 'width': 6, 'height': 12}
    circle = {'type': 'circle', 'radius': 8}
    triangle = {'type': 'triangle', 'base': 9, 'height': 5}
    print("Rectangle area:", calculate_area(rectangle))
    print("Circle area:", calculate_area(circle))
    print("Triangle area:", calculate_area(triangle))