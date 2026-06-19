import math

def calculate_area(shape):
    area = 0
    shape_type = shape.get('type')
    
    if shape_type == 'rectangle':
        length = shape.get('length', 0)
        width = shape.get('width', 0)
        area = length * width
    
    elif shape_type == 'circle':
        radius = shape.get('radius', 0)
        area = math.pi * (radius ** 2)
    
    elif shape_type == 'triangle':
        base = shape.get('base', 0)
        height = shape.get('height', 0)
        area = 0.5 * base * height
    
    elif shape_type == 'trapezoid':
        base1 = shape.get('base1', 0)
        base2 = shape.get('base2', 0)
        height = shape.get('height', 0)
        area = 0.5 * (base1 + base2) * height
    
    return area

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'length': 5, 'width': 3},
        {'type': 'circle', 'radius': 4},
        {'type': 'triangle', 'base': 6, 'height': 2},
        {'type': 'trapezoid', 'base1': 8, 'base2': 10, 'height': 5}
    ]
    
    for shape in shapes:
        print(f"Area of {shape['type']}: {calculate_area(shape)}")