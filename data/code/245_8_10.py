from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def area_of_hexagon(vertices):
    n = len(vertices)
    if n != 6:
        raise ValueError("Hexagon must have exactly 6 vertices")
    
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    
    return abs(area) / 2

def hexagons_equal_area(hexagon1, hexagon2):
    return area_of_hexagon(hexagon1) == area_of_hexagon(hexagon2)

if __name__ == '__main__':
    hexagon1 = [(0, 0), (1, 0), (1.5, sqrt(3)/2), (1, sqrt(3)), (0, sqrt(3)), (-0.5, sqrt(3)/2)]
    hexagon2 = [(2, 2), (3, 2), (3.5, 2 + sqrt(3)/2), (3, 2 + sqrt(3)), (2, 2 + sqrt(3)), (1.5, 2 + sqrt(3)/2)]
    print(hexagons_equal_area(hexagon1, hexagon2))