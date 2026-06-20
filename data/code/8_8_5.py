import math
from typing import List, Tuple

Point = Tuple[float, float]

def cross_product(o: Point, a: Point, b: Point) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def compute_convex_hull(points: List[Point]) -> List[Point]:
    if len(points) <= 2:
        return points

    points = sorted(set(points))

    if len(points) <= 2:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def calculate_convex_hull_area(coords: List[Point]) -> float:
    if not coords:
        return 0.0
    
    hull = compute_convex_hull(coords)
    
    if len(hull) < 3:
        return 0.0

    area = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]

    return abs(area) / 2.0

def haversine_area(coords: List[Point]) -> float:
    if len(coords) < 3:
        return 0.0

    hull = compute_convex_hull(coords)
    n = len(hull)
    
    if n < 3:
        return 0.0

    R = 6371000
    total_area = 0.0
    
    for i in range(n):
        j = (i + 1) % n
        k = (i + 2) % n
        
        p1 = hull[i]
        p2 = hull[j]
        p3 = hull[k]
        
        lat1, lon1 = math.radians(p1[0]), math.radians(p1[1])
        lat2, lon2 = math.radians(p2[0]), math.radians(p2[1])
        lat3, lon3 = math.radians(p3[0]), math.radians(p3[1])
        
        a = lat2 - lat1
        b = lon2 - lon1
        c = lat3 - lat2
        d = lon3 - lon2
        
        cross_prod = (math.cos(lat2) * math.sin(c) * math.cos(b)) - (math.sin(lat2) * math.cos(c) * math.sin(b))
        cross_prod += (math.sin(lat2) * math.sin(c) * math.cos(a))
        
        if cross_prod < 0:
            cross_prod = -cross_prod
        
        if cross_prod == 0:
            continue
            
        sin_val = math.sin(lat1) * math.cos(lat2) * math.sin(b)
        cos_val = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(b)
        dist_12 = 2 * R * math.atan2(math.sqrt(sin_val**2), math.sqrt(cos_val**2 + sin_val**2))
        
        sin_val_2 = math.sin(lat2) * math.cos(lat3) * math.sin(d)
        cos_val_2 = math.sin(lat2) * math.sin(lat3) + math.cos(lat2) * math.cos(lat3) * math.cos(d)
        dist_23 = 2 * R * math.atan2(math.sqrt(sin_val_2**2), math.sqrt(cos_val_2**2 + sin_val_2**2))
        
        if dist_12 == 0 or dist_23 == 0:
            continue
            
        angle = math.atan2(cross_prod, 1)
        if angle > math.pi / 2:
            angle = math.pi - angle
            
        total_area += dist_12 * dist_23 * math.sin(angle) / 2.0

    return total_area

def calculate_area(coords: List[Point], use_spherical: bool = False) -> float:
    if use_spherical:
        return haversine_area(coords)
    return calculate_convex_hull_area(coords)

if __name__ == '__main__':
    sample_coords = [
        (0, 0),
        (0, 100),
        (100, 100),
        (100, 0),
        (50, 50)
    ]
    
    planar_area = calculate_area(sample_coords, use_spherical=False)
    print(planar_area)
    
    sample_geo_coords = [
        (34.0522, -118.2437),
        (36.1699, -115.1398),
        (33.4484, -112.0740),
        (35.0844, -106.6504),
        (37.3382, -121.8863)
    ]
    
    spherical_area = calculate_area(sample_geo_coords, use_spherical=True)
    print(spherical_area)