import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def convex_hull(points):
    n = len(points)
    if n < 3:
        return []

    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i

    hull = []
    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i

        p = q

        if p == l:
            break

    return hull

def polygon_area(hull):
    area = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]

    return abs(area) / 2.0

def smallest_convex_polygon_area(points):
    hull = convex_hull(points)
    return polygon_area(hull)

if __name__ == '__main__':
    points = [(0, 3), (2, 2), (5, 1), (6, 4), (3, 3), (1, 2)]
    area = smallest_convex_polygon_area(points)
    print(area)