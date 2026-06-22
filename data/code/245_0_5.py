def shoelace_area(vertices):
    n = len(vertices)
    area = 0.5 * abs(sum(vertices[i][0] * vertices[(i + 1) % n][1] - vertices[(i + 1) % n][0] * vertices[i][1] for i in range(n)))
    return area

def shapes_equal_area(shape1, shape2):
    return shoelace_area(shape1) == shoelace_area(shape2)

if __name__ == '__main__':
    shape1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    shape2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    print(shapes_equal_area(shape1, shape2))