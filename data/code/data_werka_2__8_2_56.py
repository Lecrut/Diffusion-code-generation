def polygon_area(vertices):
    if len(vertices) < 3:
        raise ValueError("A polygon must have at least 3 vertices")
    
    def cross(v1, v2):
        return v1[0] * v2[1] - v1[1] * v2[0]
    
    area = sum(cross(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices)))
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(polygon_area(sample_vertices))