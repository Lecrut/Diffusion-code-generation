from typing import List, Tuple

def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def convex_hull(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    n = len(points)
    if n < 3:
        return []
    points.sort(key=lambda p: (p[0], p[1]))
    hull = []
    for i in range(n):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()
        hull.append(points[i])
    m = len(hull)
    for i in range(n - 2, -1, -1):
        while len(hull) > m and orientation(hull[-2], hull[-1], points[i]) != 2:
            hull.pop()
        hull.append(points[i])
    hull.pop()
    return hull

def polygon_area(points: List[Tuple[int, int]]) -> float:
    n = len(points)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

def smallest_enclosing_polygon_area(points: List[Tuple[int, int]]) -> float:
    hull = convex_hull(points)
    return polygon_area(hull)
if __name__ == '__main__':
    sample_points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    area = smallest_enclosing_polygon_area(sample_points)
    print(area)