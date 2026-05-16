import sys
def calculate_polygon_area(coordinates):
    n = len(coordinates)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2.0
if __name__ == '__main__':
    sample_coordinates = [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1)
    ]
    if len(sample_coordinates) >= 3:
        area = calculate_polygon_area(sample_coordinates)
        print(area)
    else:
        print("Not enough coordinates to form a polygon.")