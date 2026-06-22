import math
from typing import List, Tuple

EARTH_RADIUS_KM = 6371.0

def _to_cartesian(lat_deg: float, lon_deg: float) -> Tuple[float, float, float]:
    lat = math.radians(lat_deg)
    lon = math.radians(lon_deg)
    x = math.cos(lat) * math.cos(lon)
    y = math.cos(lat) * math.sin(lon)
    z = math.sin(lat)
    return x, y, z

def _cross_2d(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return a[0] * b[1] - a[1] * b[0]

def _convex_hull_2d(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    if len(points) <= 1:
        return points[:]
    points_sorted = sorted(points)
    lower = []
    for p in points_sorted:
        while len(lower) >= 2 and _cross_2d(lower[-1] - lower[-2], p - lower[-1]) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points_sorted):
        while len(upper) >= 2 and _cross_2d(upper[-1] - upper[-2], p - upper[-1]) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    return hull

def _shoelace_area_2d(points: List[Tuple[float, float]]) -> float:
    n = len(points)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

def _spherical_convex_hull_area(coords: List[Tuple[float, float]]) -> float:
    if len(coords) < 3:
        return 0.0
    cartesian = [_to_cartesian(lat, lon) for lat, lon in coords]
    vectors = [c for c in cartesian]
    n = len(vectors)
    hull_indices = []
    for i in range(n):
        is_vertex = True
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                cross = [
                    vectors[i][1] * vectors[j][2] - vectors[i][2] * vectors[j][1],
                    vectors[i][2] * vectors[j][0] - vectors[i][0] * vectors[j][2],
                    vectors[i][0] * vectors[j][1] - vectors[i][1] * vectors[j][0]
                ]
                dot = cross[0] * vectors[k][0] + cross[1] * vectors[k][1] + cross[2] * vectors[k][2]
                if dot > 1e-10:
                    is_vertex = False
                    break
            if not is_vertex:
                break
        if is_vertex:
            hull_indices.append(i)
    if len(hull_indices) < 3:
        return 0.0
    hull_points = [vectors[idx] for idx in hull_indices]
    if len(hull_points) < 3:
        return 0.0
    area = 0.0
    for i in range(len(hull_points)):
        j = (i + 1) % len(hull_points)
        cross = [
            hull_points[i][1] * hull_points[j][2] - hull_points[i][2] * hull_points[j][1],
            hull_points[i][2] * hull_points[j][0] - hull_points[i][0] * hull_points[j][2],
            hull_points[i][0] * hull_points[j][1] - hull_points[i][1] * hull_points[j][0]
        ]
        mag = math.sqrt(cross[0]**2 + cross[1]**2 + cross[2]**2)
        if mag < 1e-10:
            continue
        area += mag
    if area < 1e-10:
        return 0.0
    area_spherical = 2.0 * math.asin(area / 2.0)
    total_area = area_spherical * EARTH_RADIUS_KM**2
    return total_area

def calculate_convex_hull_area(coords: List[Tuple[float, float]]) -> float:
    if len(coords) < 3:
        return 0.0
    return _spherical_convex_hull_area(coords)

if __name__ == '__main__':
    sample_coords = [
        (40.0, -74.0),
        (41.0, -73.0),
        (42.0, -75.0),
        (39.0, -72.0),
        (40.5, -74.5)
    ]
    area = calculate_convex_hull_area(sample_coords)
    print(area)