def polygon_area(vertices):
    MIN_VERTICES = 3
    if len(vertices) < MIN_VERTICES:
        raise ValueError("A polygon must have at least 3 vertices")
    
    def cross_product(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return x1 * y2 - x2 * y1
    
    total_area = 0.0
    num_vertices = len(vertices)
    for i in range(num_vertices):
        current_vertex = vertices[i]
        next_vertex = vertices[(i + 1) % num_vertices]
        total_area += cross_product(current_vertex, next_vertex)
    
    return abs(total_area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(polygon_area(sample_vertices))