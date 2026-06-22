import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def area_of_hexagon(points):
    n = len(points)
    if n != 6:
        raise ValueError("Hexagon must have exactly 6 vertices")
    
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

def hexagons_equal_area(hexagon1, hexagon2):
    return math.isclose(area_of_hexagon(hexagon1), area_of_hexagon(hexagon2))

if __name__ == '__main__':
    hexagon1 = [(0, 0), (1, 0), (1.5, math.sqrt(3)/2), (1, 1), (0, 1), (-0.5, math.sqrt(3)/2)]
    hexagon2 = [(2, 2), (3, 2), (3.5, 2 + math.sqrt(3)/2), (3, 3), (2, 3), (1.5, 2 + math.sqrt(3)/2)]
    
    print(hexagons_equal_area(hexagon1, hexagon2))