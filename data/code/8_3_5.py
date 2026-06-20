import math

def calculate_polygon_area(vertices):
    n = len(vertices)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    return area

if __name__ == '__main__':
    vertices = [(1, 1), (3, 2), (3, 4), (1, 5)]
    area = calculate_polygon_area(vertices)
    print(area)