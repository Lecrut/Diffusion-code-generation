from typing import List, Tuple

def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def distance_squared(p: Tuple[int, int], q: Tuple[int, int]) -> int:
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

def is_valid_point(point: Tuple[int, int]) -> bool:
    if len(point) != 2 or not all(isinstance(coord, int) for coord in point):
        return False
    return True

def validate_points(points: List[Tuple[int, int]]) -> None:
    if len(points) < 3:
        raise ValueError('At least three points are required to form a polygon')
    for point in points:
        if not is_valid_point(point):
            raise ValueError(f'Invalid point: {point}')

def convex_hull_monotone_chain(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    validate_points(points)
    
    def compare(p, q):
        return (p[1], p[0]) < (q[1], q[0])

    points.sort(key=compare)

    lower_hull = []
    for point in points:
        while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], point) != 1:
            lower_hull.pop()
        lower_hull.append(point)

    upper_hull = []
    for point in reversed(points):
        while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], point) != 1:
            upper_hull.pop()
        upper_hull.append(point)

    return lower_hull[:-1] + upper_hull[:-1]

def polygon_area(hull: List[Tuple[int, int]]) -> float:
    n = len(hull)
    area = 0
    for i in range(n):
        x1, y1 = hull[i]
        x2, y2 = hull[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0

if __name__ == "__main__":
    sample_points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    hull = convex_hull_monotone_chain(sample_points)
    area = polygon_area(hull)
    print("Convex Hull:", hull)
    print("Area of the Polygon:", area)