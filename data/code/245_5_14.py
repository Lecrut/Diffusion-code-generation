def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum((vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n))))
    return area

def are_areas_equal(polygon1, polygon2):
    area1 = calculate_polygon_area(polygon1)
    area2 = calculate_polygon_area(polygon2)
    return area1 == area2
if __name__ == '__main__':
    sample1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    sample2 = [(0, 0), (3, 0), (3, 4), (0, 4)]
    result = are_areas_equal(sample1, sample2)
    print(result)