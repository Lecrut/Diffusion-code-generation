from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def area_of_hexagon(coords):
    n = len(coords)
    if n != 6:
        raise ValueError("Hexagon must have exactly 6 vertices")
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
    return abs(area) / 2.0

def hexagons_equal_area(hex1, hex2):
    return abs(area_of_hexagon(hex1) - area_of_hexagon(hex2)) < 1e-9

if __name__ == '__main__':
    hexagon1 = [(0, 0), (1, 0), (1.5, sqrt(3)/2), (1, sqrt(3)), (0, sqrt(3)), (-0.5, sqrt(3)/2)]
    hexagon2 = [(2, 2), (3, 2), (3.5, 2 + sqrt(3)/2), (3, 2 + sqrt(3)), (2, 2 + sqrt(3)), (1.5, 2 + sqrt(3)/2)]
    print(hexagons_equal_area(hexagon1, hexagon2))