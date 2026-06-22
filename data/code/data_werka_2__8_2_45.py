def polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices")
    
    def validate_vertex(vertex):
        if not isinstance(vertex, tuple) or len(vertex) != 2:
            raise ValueError("Each vertex must be a tuple of two numbers (x, y)")
        x, y = vertex
        if not all(isinstance(coord, (int, float)) for coord in [x, y]):
            raise ValueError("Vertex coordinates must be integers or floats")
    
    for vertex in vertices:
        validate_vertex(vertex)
    
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(polygon_area(sample_vertices))