def shoelace_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def shapes_equal_area(shape1, shape2):
    return shoelace_area(shape1) == shoelace_area(shape2)

if __name__ == '__main__':
    sample_shape1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    sample_shape2 = [(0, 0), (3, 0), (3, 4), (0, 4)]
    print(shapes_equal_area(sample_shape1, sample_shape2))