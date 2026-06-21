def calculate_polygon_area(vertices):
    def validate_vertices(vertices):
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        for vertex in vertices:
            if not isinstance(vertex, tuple) or len(vertex) != 2:
                raise ValueError("Each vertex must be a tuple of two numbers.")

    def cross_product(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return x1 * y2 - y1 * x2

    validate_vertices(vertices)
    n = len(vertices)
    area = 0.0
    for i in range(n):
        current_vertex = vertices[i]
        next_vertex = vertices[(i + 1) % n]
        area += cross_product(current_vertex, next_vertex)
    return abs(area) / 2.0

if __name__ == '__main__':
    polygon_vertices = [(1, 2), (4, 5), (7, 8)]
    print(calculate_polygon_area(polygon_vertices))