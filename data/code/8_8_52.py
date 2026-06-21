def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    
    def cross_product(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return x1 * y2 - y2 * x1
    
    area = 0.0
    for i in range(n):
        current_vertex = vertices[i]
        next_vertex = vertices[(i + 1) % n]
        area += cross_product(current_vertex, next_vertex)
    
    return abs(area) / 2.0

if __name__ == '__main__':
    polygon_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(calculate_polygon_area(polygon_vertices))