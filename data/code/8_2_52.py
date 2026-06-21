def polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices")
    
    def cross(v1, v2):
        return v1[0] * v2[1] - v2[0] * v1[1]
    
    total_area = sum(cross(vertices[i], vertices[(i + 1) % n]) for i in range(n))
    return abs(total_area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(polygon_area(sample_vertices))