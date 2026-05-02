import math
def shoelace_area(points):
    if len(points) < 3:
        return 0.0
    area = 0.0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = points[i]
        x2, y2 = points[j]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2.0
def calculate_convex_hull_area(coordinates):
    if len(coordinates) < 3:
        return 0.0
    points = list(coordinates)
    start_point_index = 0
    for i in range(1, len(points)):
        if points[i][1] < points[start_point_index][1] or \
           (points[i][1] == points[start_point_index][1] and points[i][0] < points[start_point_index][0]):
            start_point_index = i
    start_point = points[start_point_index]
    def polar_angle_sort_key(point):
        dx = point[0] - start_point[0]
        dy = point[1] - start_point[1]
        angle = math.atan2(dy, dx)
        distance_sq = dx*dx + dy*dy
        return (angle, distance_sq)
    sorted_points = sorted(points, key=polar_angle_sort_key)
    hull = []
    if sorted_points:
        hull.append(sorted_points[0])
        if len(sorted_points) > 1:
            hull.append(sorted_points[1])
        for i in range(2, len(sorted_points)):
            while len(hull) >= 2:
                p1 = hull[-2]
                p2 = hull[-1]
                cross_product = (p2[0] - p1[0]) * (sorted_points[i][1] - p2[1]) - \
                                (p2[1] - p1[1]) * (sorted_points[i][0] - p2[0])
                if cross_product > 0:
                    break
                else:
                    hull.pop()
            hull.append(sorted_points[i])
    return shoelace_area(hull)
if __name__ == '__main__':
    sample_coordinates = [
        (0.0, 0.0),
        (1.0, 0.0),
        (0.5, 1.0),
        (2.0, 0.5),
        (1.5, 2.0)
    ]
    area = calculate_convex_hull_area(sample_coordinates)
    print(area)