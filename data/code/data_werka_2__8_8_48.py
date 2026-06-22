def calculate_polygon_area(vertices):
    if len(vertices) < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    area = 0.0
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        area += cross_product(vertices[i], vertices[j], vertices[(j + 1) % len(vertices)])
    return abs(area) / 2.0

if __name__ == '__main__':
    polygon_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(calculate_polygon_area(polygon_vertices))