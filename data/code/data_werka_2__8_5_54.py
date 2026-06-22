import math

def validate_shape(shape):
    if 'type' not in shape:
        raise ValueError("Shape must have a type specified")
    
    shape_type = shape['type']
    if shape_type == 'rectangle':
        if 'width' not in shape or 'height' not in shape:
            raise ValueError("Rectangle must have width and height specified")
    elif shape_type == 'circle':
        if 'radius' not in shape:
            raise ValueError("Circle must have radius specified")
    elif shape_type == 'triangle':
        if 'base' not in shape or 'height' not in shape:
            raise ValueError("Triangle must have base and height specified")
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