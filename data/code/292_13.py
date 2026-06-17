import math
def calculate_polygon_perimeter(coordinates):
    perimeter = 0
    n = len(coordinates)
    if n < 2:
        return 0
    for i in range(n - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        perimeter += distance
    first_x, first_y = coordinates[0]
    last_x, last_y = coordinates[n-1]
    closing_distance = math.sqrt((first_x - last_x)**2 + (first_y - last_y)**2)
    perimeter += closing_distance
    return perimeter
if __name__ == '__main__':
    sample_coordinates = [(0, 0), (3, 0), (0, 4), (-3, 4)]
    perimeter = calculate_polygon_perimeter(sample_coordinates)
    print(perimeter)