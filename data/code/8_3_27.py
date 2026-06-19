def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0
if __name__ == '__main__':
    pentagon_vertices = [(1, 1), (4, 1), (5, 3), (3, 5), (2, 4)]
    area = polygon_area(pentagon_vertices)
    print(area)