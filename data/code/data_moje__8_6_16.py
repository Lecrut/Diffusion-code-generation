import math

def calculate_area(shape_dict):
    shape_type = shape_dict.get('type')
    if shape_type == 'circle':
        radius = shape_dict['radius']
        return math.pi * radius * radius
    elif shape_type == 'rectangle':
        width = shape_dict['width']
        height = shape_dict['height']
        return width * height
    elif shape_type == 'triangle':
        base = shape_dict['base']
        height = shape_dict['height']
        return 0.5 * base * height
    elif shape_type == 'square':
        side = shape_dict['side']
        return side * side
    elif shape_type == 'parallelogram':
        base = shape_dict['base']
        height = shape_dict['height']
        return base * height
    elif shape_type == 'trapezoid':
        a = shape_dict['a']
        b = shape_dict['b']
        height = shape_dict['height']
        return 0.5 * (a + b) * height
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

if __name__ == '__main__':
    print(calculate_area({'type': 'circle', 'radius': 5}))
    print(calculate_area({'type': 'rectangle', 'width': 4, 'height': 6}))
    print(calculate_area({'type': 'triangle', 'base': 10, 'height': 5}))
    print(calculate_area({'type': 'square', 'side': 7}))
    print(calculate_area({'type': 'parallelogram', 'base': 8, 'height': 3}))
    print(calculate_area({'type': 'trapezoid', 'a': 5, 'b': 7, 'height': 4}))