import math
from typing import List, Tuple

def _cross_2d(o: Tuple[float, float], a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def _convex_hull(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    
    lower = []
    for p in points:
        while len(lower) >= 2 and _cross_2d(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and _cross_2d(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

def _shoelace_area(hull: List[Tuple[float, float]]) -> float:
    n = len(hull)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    return abs(area) / 2.0

def calculate_convex_hull_area(coordinates: List[Tuple[float, float]]) -> float:
    hull = _convex_hull(coordinates)
    return _shoelace_area(hull)

if __name__ == '__main__':
    sample_coordinates = [
        (0.0, 0.0),
        (1.0, 0.0),
        (1.0, 1.0),
        (0.0, 1.0),
        (0.5, 0.5)
    ]
    result = calculate_convex_hull_area(sample_coordinates)
    print(result)