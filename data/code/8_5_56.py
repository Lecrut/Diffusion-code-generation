import math

def calculate_area(shape):
    shape_type = shape.get('type')
    if shape_type == 'rectangle':
        width = shape.get('width')
        height = shape.get('height')
        if width is None or height is None:
            raise ValueError("Rectangle requires both width and height")
        return width * height
    elif shape_type == 'circle':
        radius = shape.get('radius')
        if radius is None:
            raise ValueError("Circle requires a radius")
        return math.pi * (radius ** 2)
    elif shape_type == 'triangle':
        base = shape.get('base')
        height = shape.get('height')
        if base is None or height is None:
            raise ValueError("Triangle requires both base and height")
        return 0.5 * base * height
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    rectangle = {'type': 'rectangle', 'width': 6, 'height': 12}
    circle = {'type': 'circle', 'radius': 8}
    triangle = {'type': 'triangle', 'base': 10, 'height': 5}
    try:
        print("Rectangle area:", calculate_area(rectangle))
        print("Circle area:", calculate_area(circle))
        print("Triangle area:", calculate_area(triangle))
    except ValueError as e:
        print(e)