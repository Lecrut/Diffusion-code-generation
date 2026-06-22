import math

def calculate_area(shape):
    area = 0
    if shape['type'] == 'rectangle':
        area = shape['width'] * shape['height']
    elif shape['type'] == 'circle':
        area = math.pi * (shape['radius'] ** 2)
    elif shape['type'] == 'triangle':
        area = 0.5 * shape['base'] * shape['height']
    return area

if __name__ == '__main__':
    shapes = [
        {'type': 'rectangle', 'width': 5, 'height': 3},
        {'type': 'circle', 'radius': 4},
        {'type': 'triangle', 'base': 6, 'height': 2}
    ]
    
    for shape in shapes:
        print(f"Area of {shape['type']}: {calculate_area(shape)}")