import math
from typing import List, Tuple

Point = Tuple[float, float]

def cross_product(o: Point, a: Point, b: Point) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def dist_sq(a: Point, b: Point) -> float:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def convex_hull_area(points: List[Point]) -> float:
    n = len(points)
    if n < 3:
        return 0.0

    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))

    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1]
    h_n = len(hull)
    if h_n < 3:
        return 0.0

    area = 0.0
    for i in range(h_n):
        j = (i + 1) % h_n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    
    return abs(area) / 2.0

if __name__ == '__main__':
    points = [(0, 0), (10, 0), (10, 10), (0, 10)]
    area = convex_hull_area(points)
    print(area)