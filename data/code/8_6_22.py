import math

def calculate_area(shape):
    shape_type = shape.get('type')
    if shape_type == 'rectangle':
        width = shape['width']
        height = shape['height']
        return width * height
    elif shape_type == 'circle':
        radius = shape['radius']
        return math.pi * (radius ** 2)
    elif shape_type == 'triangle':
        base = shape['base']
        height = shape['height']
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle_area = calculate_area({'type': 'rectangle', 'width': 5, 'height': 10})
    circle_area = calculate_area({'type': 'circle', 'radius': 7})
    triangle_area = calculate_area({'type': 'triangle', 'base': 8, 'height': 6})

    print("Rectangle Area:", rectangle_area)
    print("Circle Area:", circle_area)
    print("Triangle Area:", triangle_area)