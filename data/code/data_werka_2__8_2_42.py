def polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices")
    
    def cross_product(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return x1 * y2 - x2 * y1
    
    total_area = 0.0
    for i in range(n):
        current_vertex = vertices[i]
        next_vertex = vertices[(i + 1) % n]
        total_area += cross_product(current_vertex, next_vertex)
    
    return abs(total_area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(1, 1), (4, 5), (7, 1)]
    print(polygon_area(sample_vertices))