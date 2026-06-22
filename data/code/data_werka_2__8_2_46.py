def polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices")
    
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(0, 0), (5, 0), (5, 2), (0, 2)]
    print(polygon_area(sample_vertices))