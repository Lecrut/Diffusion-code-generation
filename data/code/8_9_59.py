from typing import List, Tuple

def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def distance_squared(p: Tuple[int, int], q: Tuple[int, int]) -> int:
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

def convex_hull(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    n = len(points)
    if n < 3:
        raise ValueError('At least three points are required to form a polygon')
    
    start = min(points, key=lambda x: (x[0], -x[1]))
    points.remove(start)
    sorted_points = sorted(points, key=lambda p: (orientation(start, p, (start[0] + 1, start[1])), distance_squared(p, start)))
    hull = [start]
    
    for point in sorted_points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) != 1:
            hull.pop()
        hull.append(point)
    
    return hull

def polygon_area(points: List[Tuple[int, int]]) -> float:
    n = len(points)
    if n < 3:
        raise ValueError('At least three points are required to form a polygon')
    
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

if __name__ == "__main__":
    sample_points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2)]
    hull = convex_hull(sample_points)
    area = polygon_area(hull)
    print("Convex Hull:", hull)
    print("Area of Convex Hull:", area)