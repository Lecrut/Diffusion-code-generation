def validate_vertex(vertex):
    if not isinstance(vertex, tuple) or len(vertex) != 2:
        raise ValueError("Each vertex must be a tuple of two numbers.")
    for coord in vertex:
        if not isinstance(coord, (int, float)):
            raise ValueError("All coordinates must be integers or floats.")

def triangle_area(p1, p2, p3):
    validate_vertex(p1)
    validate_vertex(p2)
    validate_vertex(p3)
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    area = triangle_area(*vertices)
    print(area)