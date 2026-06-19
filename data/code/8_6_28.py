import math

def calculate_area(shape):
    shape_type = shape.get('type')
    if shape_type == 'circle':
        radius = shape['radius']
        return math.pi * radius ** 2
    elif shape_type == 'rectangle':
        width = shape['width']
        height = shape['height']
        return width * height
    elif shape_type == 'triangle':
        base = shape['base']
        height = shape['height']
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    shapes = [
        {'type': 'circle', 'radius': 5},
        {'type': 'rectangle', 'width': 4, 'height': 6},
        {'type': 'triangle', 'base': 3, 'height': 7}
    ]
    
    for shape in shapes:
        area = calculate_area(shape)
        print(f"The area of the {shape['type']} is: {area}")