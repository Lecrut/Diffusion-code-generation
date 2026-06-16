import math
def calculate_perimeter(coordinates):
    perimeter = 0
    n = len(coordinates)
    if n < 2:
        return 0
    for i in range(n - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        perimeter += distance
    x1, y1 = coordinates[n-1]
    x2, y2 = coordinates[0]
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    perimeter += distance
    return perimeter
if __name__ == '__main__':
    polygon_coords = [(0, 0), (3, 0), (0, 4), (-3, 4)]
    perimeter = calculate_perimeter(polygon_coords)
    print(perimeter)