def calculate_area(params: dict) -> float:
    shape_type = params.get('type')
    
    if shape_type == 'circle':
        radius = params.get('radius', 0)
        return 3.141592653589793 * radius * radius
    
    if shape_type == 'rectangle':
        width = params.get('width', 0)
        height = params.get('height', 0)
        return width * height
    
    if shape_type == 'triangle':
        base = params.get('base', 0)
        height = params.get('height', 0)
        return 0.5 * base * height
    
    if shape_type == 'square':
        side = params.get('side', 0)
        return side * side
    
    if shape_type == 'trapezoid':
        a = params.get('a', 0)
        b = params.get('b', 0)
        h = params.get('height', 0)
        return 0.5 * (a + b) * h
    
    raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    circle_params = {'type': 'circle', 'radius': 5}
    rect_params = {'type': 'rectangle', 'width': 4, 'height': 7}
    tri_params = {'type': 'triangle', 'base': 10, 'height': 6}
    square_params = {'type': 'square', 'side': 3}
    trap_params = {'type': 'trapezoid', 'a': 5, 'b': 9, 'height': 4}
    
    print(calculate_area(circle_params))
    print(calculate_area(rect_params))
    print(calculate_area(tri_params))
    print(calculate_area(square_params))
    print(calculate_area(trap_params))