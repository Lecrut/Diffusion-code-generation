def calculate_polygon_area(vertices):
    if len(vertices) < 3:
        return 0.0
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    return area

if __name__ == '__main__':
    square = [(0, 0), (4, 0), (4, 4), (0, 4)]
    triangle = [(0, 0), (4, 0), (2, 3)]
    pentagon = [(0, 0), (2, 1), (3, 3), (1, 4), (-1, 3)]
    
    print(calculate_polygon_area(square))
    print(calculate_polygon_area(triangle))
    print(calculate_polygon_area(pentagon))