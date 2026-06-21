def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices")
    
    total_sum = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        cross_term = x1 * y2 - x2 * y1
        total_sum += cross_term
    
    return abs(total_sum) / 2.0

if __name__ == '__main__':
    sample_vertices = [(3, 1), (5, 7), (9, 4)]
    print(calculate_polygon_area(sample_vertices))