def calculate_triangle_area(p1, p2, p3):
    def validate_vertex(vertex):
        if not isinstance(vertex, tuple) or len(vertex) != 2:
            raise ValueError("Each vertex must be a tuple of two numbers.")
        x, y = vertex
        if not all(isinstance(coord, (int, float)) for coord in [x, y]):
            raise ValueError("All coordinates must be integers or floats.")

    validate_vertex(p1)
    validate_vertex(p2)
    validate_vertex(p3)

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

if __name__ == '__main__':
    vertices = [(0, 0), (4, 0), (2, 3)]
    try:
        area = calculate_triangle_area(*vertices)
        print(area)
    except ValueError as e:
        print(e)