from math import sqrt

def calculate_hexagon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = vertices[i]
        x2, y2 = vertices[j]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0

def hexagons_equal_area(hexagon1, hexagon2):
    area1 = calculate_hexagon_area(hexagon1)
    area2 = calculate_hexagon_area(hexagon2)
    return area1 == area2

if __name__ == '__main__':
    hexagon1 = [(0, 0), (1, 0), (1.5, sqrt(3)/2), (1, 1), (0, 1), (-0.5, sqrt(3)/2)]
    hexagon2 = [(2, 2), (3, 2), (3.5, 2 + sqrt(3)/2), (3, 3), (2, 3), (1.5, 2 + sqrt(3)/2)]
    print(hexagons_equal_area(hexagon1, hexagon2))