def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    
    def cross_product(x1, y1, x2, y2):
        return x1 * y2 - y1 * x2
    
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += cross_product(x1, y1, x2, y2)
    
    return abs(area) / 2.0

if __name__ == '__main__':
    polygon_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(calculate_polygon_area(polygon_vertices))