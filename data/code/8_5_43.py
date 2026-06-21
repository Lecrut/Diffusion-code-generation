def calculate_area(shape):
    if shape['type'] == 'rectangle':
        width = shape.get('width')
        height = shape.get('height')
        if width is None or height is None:
            raise ValueError("Rectangle requires 'width' and 'height'")
        return width * height
    elif shape['type'] == 'circle':
        radius = shape.get('radius')
        if radius is None:
            raise ValueError("Circle requires 'radius'")
        import math
        return math.pi * radius ** 2
    elif shape['type'] == 'triangle':
        base = shape.get('base')
        height = shape.get('height')
        if base is None or height is None:
            raise ValueError("Triangle requires 'base' and 'height'")
        return 0.5 * base * height
    else:
        raise ValueError(f"Unsupported shape type: {shape['type']}")

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'width': 5, 'height': 10},
        {'type': 'circle', 'radius': 7},
        {'type': 'triangle', 'base': 4, 'height': 3}
    ]
    
    for shape in shapes:
        try:
            area = calculate_area(shape)
            print(f"The area of the {shape['type']} is: {area}")
        except ValueError as e:
            print(e)