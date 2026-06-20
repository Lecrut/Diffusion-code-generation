import math

def calculate_convex_hull_area(coordinates):
    n = len(coordinates)
    if n < 3:
        return 0.0

    min_x = n - 1
    for i in range(n):
        if coordinates[i][0] < coordinates[min_x][0]:
            min_x = i

    pivot = coordinates[min_x]
    
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def angle_key(point):
        dx = point[0] - pivot[0]
        dy = point[1] - pivot[1]
        return math.atan2(dy, dx)

    points = coordinates[:min_x] + coordinates[min_x+1:]
    points.sort(key=angle_key)
    
    if not points:
        return 0.0

    hull = [pivot]
    
    for p in points:
        while len(hull) > 1 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    if len(hull) < 3:
        return 0.0

    area = 0.0
    m = len(hull)
    for i in range(m):
        j = (i + 1) % m
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]

    return abs(area) / 2.0

if __name__ == '__main__':
    sample_coordinates = [
        (0.0, 0.0),
        (0.0, 1.0),
        (1.0, 1.0),
        (1.0, 0.0),
        (0.5, 0.5)
    ]
    result = calculate_convex_hull_area(sample_coordinates)
    print(result)