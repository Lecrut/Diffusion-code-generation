import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def convex_hull(points):
    n = len(points)
    if n < 3:
        raise ValueError("At least three points are required to form a polygon")
    
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    
    hull = []
    p = l
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

def polygon_area(points):
    area = 0.0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    area = abs(area) / 2.0
    return area

def smallest_convex_polygon_area(points):
    hull = convex_hull(points)
    return polygon_area(hull)

if __name__ == '__main__':
    sample_points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1)]
    area = smallest_convex_polygon_area(sample_points)
    print(area)