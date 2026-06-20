def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) * 0.5
    area = round(area, 10)
    return area

if __name__ == '__main__':
    sample_vertices = [(0, 0), (4, 0), (4, 4), (0, 4)]
    result = calculate_polygon_area(sample_vertices)
    print(result)