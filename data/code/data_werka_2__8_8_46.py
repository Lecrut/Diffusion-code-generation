def calculate_polygon_area(vertices):
    def is_valid_vertex(v):
        return isinstance(v, tuple) and len(v) == 2 and all(isinstance(coord, (int, float)) for coord in v)
    
    if not vertices:
        raise ValueError("Vertices list cannot be empty.")
    
    if len(vertices) < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    
    if not all(is_valid_vertex(v) for v in vertices):
        raise ValueError("All vertices must be tuples of two numbers (x, y).")
    
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y2 * x1
    
    return abs(area) / 2.0

if __name__ == '__main__':
    polygon_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(calculate_polygon_area(polygon_vertices))