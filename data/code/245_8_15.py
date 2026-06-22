import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def hexagon_area(vertices):
    if len(vertices) != 6:
        raise ValueError("Hexagon must have exactly 6 vertices")
    
    area = 0
    n = len(vertices)
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def compare_hexagon_areas(hexagon1, hexagon2):
    area1 = hexagon_area(hexagon1)
    area2 = hexagon_area(hexagon2)
    epsilon = 1e-9
    return abs(area1 - area2) < epsilon

if __name__ == '__main__':
    hex1 = [(0, 0), (1, 0), (1.5, math.sqrt(3)/2), (1, math.sqrt(3)), (0, math.sqrt(3)), (-0.5, math.sqrt(3)/2)]
    hex2 = [(2, 2), (3, 2), (3.5, 3.7498979591836735), (3, 5), (2, 5), (1.5, 3.7498979591836735)]
    print(f"Test 1 (Expected False): {compare_hexagon_areas(hex1, hex2)}")
    
    hex3 = [(0, 0), (1, 0), (1.5, math.sqrt(3)/2), (1, math.sqrt(3)), (0, math.sqrt(3)), (-0.5, math.sqrt(3)/2)]
    hex4 = [(0, 0), (2, 0), (3, 0), (3, 2), (2, 2), (0, 2)]
    print(f"Test 2 (Expected True): {compare_hexagon_areas(hex3, hex4)}")
    
    hex5 = [(1, 0), (2, -math.sqrt(3)), (4, -math.sqrt(3)), (3, 0), (4, math.sqrt(3)), (2, math.sqrt(3))]
    hex6 = [(3, 0), (4, -math.sqrt(3)), (6, -math.sqrt(3)), (5, 0), (6, math.sqrt(3)), (4, math.sqrt(3))]
    print(f"Test 3 (Expected True): {compare_hexagon_areas(hex5, hex6)}")