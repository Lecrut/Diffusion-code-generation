import math

def calculate_area(shape):
    if shape['type'] == 'rectangle':
        return shape['width'] * shape['height']
    elif shape['type'] == 'circle':
        return math.pi * (shape['radius'] ** 2)
    elif shape['type'] == 'triangle':
        return 0.5 * shape['base'] * shape['height']
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'width': 5, 'height': 3},
        {'type': 'circle', 'radius': 4},
        {'type': 'triangle', 'base': 6, 'height': 2}
    ]
    
    for shape in shapes:
        print(f"Area of {shape['type']}: {calculate_area(shape)}")