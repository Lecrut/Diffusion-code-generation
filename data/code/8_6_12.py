import math

def calculate_area(shape_params):
    shape_type = shape_params.get('type')
    if shape_type == 'circle':
        radius = shape_params['radius']
        return math.pi * radius ** 2
    elif shape_type == 'rectangle':
        width = shape_params['width']
        height = shape_params['height']
        return width * height
    elif shape_type == 'triangle':
        base = shape_params['base']
        height = shape_params['height']
        return 0.5 * base * height
    elif shape_type == 'square':
        side = shape_params['side']
        return side ** 2
    elif shape_type == 'trapezoid':
        a = shape_params['a']
        b = shape_params['b']
        height = shape_params['height']
        return 0.5 * (a + b) * height
    elif shape_type == 'ellipse':
        a = shape_params['a']
        b = shape_params['b']
        return math.pi * a * b
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

if __name__ == '__main__':
    circle_area = calculate_area({'type': 'circle', 'radius': 5})
    print(circle_area)
    
    rectangle_area = calculate_area({'type': 'rectangle', 'width': 4, 'height': 6})
    print(rectangle_area)
    
    triangle_area = calculate_area({'type': 'triangle', 'base': 10, 'height': 5})
    print(triangle_area)
    
    square_area = calculate_area({'type': 'square', 'side': 7})
    print(square_area)
    
    trapezoid_area = calculate_area({'type': 'trapezoid', 'a': 8, 'b': 12, 'height': 5})
    print(trapezoid_area)
    
    ellipse_area = calculate_area({'type': 'ellipse', 'a': 5, 'b': 3})
    print(ellipse_area)