def shoelace_area(vertices):
    area = 0
    n = len(vertices)
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def are_areas_equal(shape1, shape2):
    return shoelace_area(shape1) == shoelace_area(shape2)

if __name__ == '__main__':
    shape1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    shape2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    print(are_areas_equal(shape1, shape2))