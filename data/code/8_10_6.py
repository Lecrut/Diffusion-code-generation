import math
def shoelace_area(points):
    n = len(points)
    if n < 3:
        return 0.0
    sum1 = 0.0
    sum2 = 0.0
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = points[i]
        x2, y2 = points[j]
        sum1 += x1 * y2
        sum2 += y1 * x2
    area = 0.5 * abs(sum1 - sum2)
    return area
def convex_hull(points):
    if len(points) <= 2:
        return points
    start_point = min(points, key=lambda p: (p[1], p[0]))
    def angle_sort_key(p):
        dx = p[0] - start_point[0]
        dy = p[1] - start_point[1]
        angle = math.atan2(dy, dx)
        distance = (dx**2 + dy**2)
        return (angle, distance)
    sorted_points = sorted(points, key=angle_sort_key)
    hull = []
    for p in sorted_points:
        while len(hull) >= 2:
            p1 = hull[-2]
            p2 = hull[-1]
            cross_product = (p2[0] - p1[0]) * (p[1] - p1[1]) - (p2[1] - p1[1]) * (p[0] - p1[0])
            if cross_product > 0:
                break
            else:
                hull.pop()
        hull.append(p)
    return hull
def calculate_convex_hull_area(coordinates):
    if len(coordinates) < 3:
        return 0.0
    hull_points = convex_hull(coordinates)
    return shoelace_area(hull_points)
if __name__ == '__main__':
    sample_coordinates = [
        (0.0, 0.0),
        (1.0, 0.0),
        (0.0, 1.0),
        (1.0, 1.0),
        (0.5, 0.5),
        (2.0, 0.0)
    ]
    area = calculate_convex_hull_area(sample_coordinates)
    print(area)