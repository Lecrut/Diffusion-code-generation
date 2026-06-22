import math

def calculate_area(shape):
    shape_type = shape.get('type')
    if shape_type == 'rectangle':
        length = shape.get('length', 0)
        width = shape.get('width', 0)
        return length * width
    elif shape_type == 'circle':
        radius = shape.get('radius', 0)
        return math.pi * radius ** 2
    elif shape_type == 'triangle':
        base = shape.get('base', 0)
        height = shape.get('height', 0)
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'length': 5, 'width': 3},
        {'type': 'circle', 'radius': 7},
        {'type': 'triangle', 'base': 4, 'height': 6}
    ]
    
    for shape in shapes:
        area = calculate_area(shape)
        print(f"The area of the {shape['type']} is: {area}")