import math

def calculate_area(shape):
    shape_type = shape.get('type')
    if shape_type not in SHAPE_HANDLERS:
        raise ValueError(f"Unsupported shape type: {shape_type}")
    
    return SHAPE_HANDLERS[shape_type](shape)

def handle_rectangle(shape):
    width = shape.get('width')
    height = shape.get('height')
    return width * height

def handle_circle(shape):
    radius = shape.get('radius')
    return math.pi * (radius ** 2)

def handle_triangle(shape):
    base = shape.get('base')
    height = shape.get('height')
    return 0.5 * base * height

SHAPE_HANDLERS = {
    'rectangle': handle_rectangle,
    'circle': handle_circle,
    'triangle': handle_triangle
}

if __name__ == '__main__':
    rectangle = {'type': 'rectangle', 'width': 5, 'height': 10}
    circle = {'type': 'circle', 'radius': 7}
    triangle = {'type': 'triangle', 'base': 8, 'height': 6}
    
    print("Rectangle area:", calculate_area(rectangle))
    print("Circle area:", calculate_area(circle))
    print("Triangle area:", calculate_area(triangle))