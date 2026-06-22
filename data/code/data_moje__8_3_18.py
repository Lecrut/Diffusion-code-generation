import math

def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    area_result = calculate_polygon_area(sample_vertices)
    print(area_result)