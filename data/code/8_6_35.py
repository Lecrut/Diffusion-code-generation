import math

def calculate_area(shape):
    if shape['type'] == 'rectangle':
        width = shape.get('width', 0)
        height = shape.get('height', 0)
        return width * height
    elif shape['type'] == 'circle':
        radius = shape.get('radius', 0)
        return math.pi * (radius ** 2)
    elif shape['type'] == 'triangle':
        base = shape.get('base', 0)
        height = shape.get('height', 0)
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'width': 5, 'height': 10},
        {'type': 'circle', 'radius': 7},
        {'type': 'triangle', 'base': 8, 'height': 6}
    ]
    
    for shape in shapes:
        area = calculate_area(shape)
        print(f"The area of a {shape['type']} is: {area}")