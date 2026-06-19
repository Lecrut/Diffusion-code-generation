def calculate_area(shape):
    area = 0
    if shape['type'] == 'rectangle':
        area = shape['width'] * shape['height']
    elif shape['type'] == 'circle':
        import math
        area = math.pi * (shape['radius'] ** 2)
    elif shape['type'] == 'triangle':
        area = 0.5 * shape['base'] * shape['height']
    return area

if __name__ == '__main__':
    rectangle = {'type': 'rectangle', 'width': 5, 'height': 10}
    circle = {'type': 'circle', 'radius': 7}
    triangle = {'type': 'triangle', 'base': 8, 'height': 6}

    print("Rectangle Area:", calculate_area(rectangle))
    print("Circle Area:", calculate_area(circle))
    print("Triangle Area:", calculate_area(triangle))