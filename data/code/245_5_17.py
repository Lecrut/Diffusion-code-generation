import math

def shoelace_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def are_areas_equal(shape1, shape2):
    if len(shape1) != len(shape2):
        return False
    area1 = shoelace_area(shape1)
    area2 = shoelace_area(shape2)
    return math.isclose(area1, area2)
if __name__ == '__main__':
    polygon1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    result = are_areas_equal(polygon1, polygon2)
    print(result)