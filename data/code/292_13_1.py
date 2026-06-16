import math
def calculate_polygon_perimeter(coordinates):
    perimeter = 0
    n = len(coordinates)
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        perimeter += distance
    return perimeter
if __name__ == '__main__':
    polygon_coords = [(0, 0), (3, 0), (0, 4)]
    perimeter = calculate_polygon_perimeter(polygon_coords)
    print(perimeter)