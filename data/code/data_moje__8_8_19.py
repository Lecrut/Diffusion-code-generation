import math
from typing import List, Tuple

def cross_product(o: Tuple[float, float], a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def compute_convex_hull(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    if len(points) <= 1:
        return points
    
    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))
    
    lower_hull = []
    for p in sorted_points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)
    
    upper_hull = []
    for p in reversed(sorted_points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)
    
    if len(lower_hull) > 1:
        lower_hull.pop()
    if len(upper_hull) > 1:
        upper_hull.pop()
        
    return lower_hull + upper_hull

def shoelace_area(hull: List[Tuple[float, float]]) -> float:
    n = len(hull)
    if n < 3:
        return 0.0
    
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    
    return abs(area) / 2.0

def calculate_convex_hull_area_degrees(coordinates: List[Tuple[float, float]]) -> float:
    if len(coordinates) < 3:
        return 0.0
    
    hull = compute_convex_hull(coordinates)
    
    if len(hull) < 3:
        return 0.0
    
    return shoelace_area(hull)

if __name__ == '__main__':
    sample_coords = [
        (34.0, -118.0),
        (34.1, -118.1),
        (34.2, -118.0),
        (34.1, -117.9),
        (34.05, -118.05)
    ]
    
    area = calculate_convex_hull_area_degrees(sample_coords)
    print(area)