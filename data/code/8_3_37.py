def polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    
    total = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        total += x1 * y2 - y1 * x2
    
    return abs(total) / 2.0

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(polygon_area(sample_vertices))