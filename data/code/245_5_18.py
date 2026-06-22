def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        x_i, y_i = vertices[i]
        x_j, y_j = vertices[j]
        area += x_i * y_j - y_i * x_j
    return abs(area) / 2.0

def are_areas_equal(polygon1, polygon2):
    area1 = calculate_polygon_area(polygon1)
    area2 = calculate_polygon_area(polygon2)
    return area1 == area2

if __name__ == '__main__':
    polygon1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    
    result = are_areas_equal(polygon1, polygon2)
    print(result)