def validate_vertices(p1, p2, p3):
    if not all(isinstance(v, tuple) and len(v) == 2 for v in (p1, p2, p3)):
        raise ValueError("Each vertex must be a tuple of two elements.")
    for x, y in (p1, p2, p3):
        if not all(isinstance(coord, (int, float)) for coord in (x, y)):
            raise ValueError("All coordinates must be integers or floats.")

def triangle_area(p1, p2, p3):
    validate_vertices(p1, p2, p3)
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    area = triangle_area(*vertices)
    print(area)