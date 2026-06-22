import math

def calculate_area(shape):
    if shape['type'] == 'rectangle':
        return shape['width'] * shape['height']
    elif shape['type'] == 'circle':
        return math.pi * (shape['radius'] ** 2)
    elif shape['type'] == 'triangle':
        return 0.5 * shape['base'] * shape['height']
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle = {'type': 'rectangle', 'width': 4, 'height': 6}
    circle = {'type': 'circle', 'radius': 3}
    triangle = {'type': 'triangle', 'base': 5, 'height': 7}

    print("Rectangle area:", calculate_area(rectangle))
    print("Circle area:", calculate_area(circle))
    print("Triangle area:", calculate_area(triangle))