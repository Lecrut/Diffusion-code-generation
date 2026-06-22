def calculate_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum((vertices[i][0] * vertices[(i + 1) % n][1] - vertices[i][1] * vertices[(i + 1) % n][0] for i in range(n))))
    return area

def are_areas_equal(shape1, shape2):
    area1 = calculate_area(shape1)
    area2 = calculate_area(shape2)
    return abs(area1 - area2) < 1e-09
if __name__ == '__main__':
    polygon1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    print(are_areas_equal(polygon1, polygon2))