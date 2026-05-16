def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0
if __name__ == '__main__':
    sample_vertices = [
        [2, 4],
        [4, 6],
        [6, 2],
        [4, 0],
        [2, 2]
    ]
    area = polygon_area(sample_vertices)
    print(area)