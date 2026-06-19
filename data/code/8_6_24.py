def calculate_area(shape):
    shape_type = shape.get('type')
    if shape_type == 'rectangle':
        width = shape['width']
        height = shape['height']
        return width * height
    elif shape_type == 'circle':
        radius = shape['radius']
        import math
        return math.pi * (radius ** 2)
    elif shape_type == 'triangle':
        base = shape['base']
        height = shape['height']
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
        print(f"Area of {shape['type']}: {calculate_area(shape)}")