def calculate_area(shape_params):
    shape_type = shape_params.get('shape')
    if shape_type == 'rectangle':
        length = shape_params.get('length')
        width = shape_params.get('width')
        return length * width
    elif shape_type == 'circle':
        radius = shape_params.get('radius')
        return 3.141592653589793 * radius * radius
    elif shape_type == 'triangle':
        base = shape_params.get('base')
        height = shape_params.get('height')
        return 0.5 * base * height
    elif shape_type == 'square':
        side = shape_params.get('side')
        return side * side
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    rect_area = calculate_area({'shape': 'rectangle', 'length': 5, 'width': 3})
    circle_area = calculate_area({'shape': 'circle', 'radius': 2})
    triangle_area = calculate_area({'shape': 'triangle', 'base': 4, 'height': 6})
    square_area = calculate_area({'shape': 'square', 'side': 7})
    print(rect_area)
    print(circle_area)
    print(triangle_area)
    print(square_area)