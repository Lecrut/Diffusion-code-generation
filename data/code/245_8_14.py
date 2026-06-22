import math

def calculate_hexagon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += abs(x1 * y2 - x2 * y1)
    return abs(area) / 2

def hexagons_have_equal_areas(hexagon1, hexagon2):
    area1 = calculate_hexagon_area(hexagon1)
    area2 = calculate_hexagon_area(hexagon2)
    return math.isclose(area1, area2)

if __name__ == '__main__':
    hexagon1 = [(0, 0), (1, 0), (1.5, math.sqrt(3)/2), (1, math.sqrt(3)), (0, math.sqrt(3)), (-0.5, math.sqrt(3)/2)]
    hexagon2 = [(2, 2), (3, 2), (3.5, 2 + math.sqrt(3)/2), (3, 3 + math.sqrt(3)), (2, 3 + math.sqrt(3)), (1.5, 2 + math.sqrt(3)/2)]
    print(hexagons_have_equal_areas(hexagon1, hexagon2))