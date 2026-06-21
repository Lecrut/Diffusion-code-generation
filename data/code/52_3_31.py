def calculate_area(dimensions):
    if len(dimensions) == 3:
        return calculate_triangle_area(dimensions)
    elif len(dimensions) == 8:
        return calculate_quadrilateral_area(dimensions)
    else:
        raise ValueError('Unsupported number of dimensions for area calculation')

def validate_triangle_dimensions(dimensions):
    a, b, c = dimensions
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('Invalid triangle dimensions')

def calculate_triangle_area(sides):
    validate_triangle_dimensions(sides)
    a, b, c = sides
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def validate_quadrilateral_vertices(vertices):
    if len(vertices) != 8:
        raise ValueError('Quadrilateral must have exactly 8 dimensions')

def calculate_quadrilateral_area(vertices):
    validate_quadrilateral_vertices(vertices)
    x1, y1, x2, y2, x3, y3, x4, y4 = vertices
    return abs((x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 - y1 * x2 - y2 * x3 - y3 * x4 - y4 * x1) / 2)

if __name__ == '__main__':
    triangle_dimensions = [3, 4, 5]
    quadrilateral_vertices = [0, 0, 4, 0, 4, 3, 0, 3]
    print('Triangle Area:', calculate_area(triangle_dimensions))
    print('Quadrilateral Area:', calculate_area(quadrilateral_vertices))