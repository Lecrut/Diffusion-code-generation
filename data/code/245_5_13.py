def shoelace_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
    return area

def are_areas_equal(polygon1, polygon2):
    area1 = shoelace_area(polygon1)
    area2 = shoelace_area(polygon2)
    return abs(area1 - area2) < 1e-9

if __name__ == '__main__':
    poly1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    poly2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    print(are_areas_equal(poly1, poly2))