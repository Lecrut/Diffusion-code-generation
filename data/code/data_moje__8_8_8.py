import math

def calculate_convex_hull_area(coords):
    if not coords:
        return 0.0
    hull_points = _compute_convex_hull(coords)
    if len(hull_points) < 3:
        return 0.0
    return _shoelace_area(hull_points)

def _compute_convex_hull(points):
    n = len(points)
    if n <= 1:
        return list(points)
    points = sorted(points)
    if len(points) == 2:
        return points if points[0] != points[1] else [points[0]]
    lower = []
    for p in points:
        while len(lower) >= 2:
            cross = _cross(lower[-2], lower[-1], p)
            if cross <= 0:
                lower.pop()
            else:
                break
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2:
            cross = _cross(upper[-2], upper[-1], p)
            if cross <= 0:
                upper.pop()
            else:
                break
        upper.append(p)
    lower.pop()
    upper.pop()
    return lower + upper

def _cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def _shoelace_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_coords = [
        (0.0, 0.0),
        (1.0, 0.0),
        (1.0, 1.0),
        (0.0, 1.0),
        (0.5, 0.5)
    ]
    result = calculate_convex_hull_area(sample_coords)
    print(result)