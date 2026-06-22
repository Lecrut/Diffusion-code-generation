import math

def calculate_area(shape):
    shape_type = shape.get('type')
    
    if shape_type == 'rectangle':
        width = shape.get('width', 0)
        height = shape.get('height', 0)
        return width * height
    
    elif shape_type == 'circle':
        radius = shape.get('radius', 0)
        return math.pi * (radius ** 2)
    
    elif shape_type == 'triangle':
        base = shape.get('base', 0)
        height = shape.get('height', 0)
        return 0.5 * base * height
    
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    rectangle = {'type': 'rectangle', 'width': 3, 'height': 7}
    circle = {'type': 'circle', 'radius': 4}
    triangle = {'type': 'triangle', 'base': 6, 'height': 5}
    
    print("Rectangle area:", calculate_area(rectangle))
    print("Circle area:", calculate_area(circle))
    print("Triangle area:", calculate_area(triangle))