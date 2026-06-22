import math
from typing import List, Tuple

def _to_cartesian(lat: float, lon: float) -> Tuple[float, float, float]:
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    x = math.cos(lat_rad) * math.cos(lon_rad)
    y = math.cos(lat_rad) * math.sin(lon_rad)
    z = math.sin(lat_rad)
    return (x, y, z)

def _cross_2d(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return a[0] * b[1] - a[1] * b[0]

def _convex_hull_2d(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    points = sorted(set(points))
    if len(points) <= 1:
        return list(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and _cross_2d((lower[-1][0] - lower[-2][0], lower[-1][1] - lower[-2][1]), (p[0] - lower[-1][0], p[1] - lower[-1][1])) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and _cross_2d((upper[-1][0] - upper[-2][0], upper[-1][1] - upper[-2][1]), (p[0] - upper[-1][0], p[1] - upper[-1][1])) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def _shoelace_area_2d(poly: List[Tuple[float, float]]) -> float:
    n = len(poly)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += poly[i][0] * poly[j][1]
        area -= poly[j][0] * poly[i][1]
    return abs(area) / 2.0

def _compute_3d_convex_hull_area(points_3d: List[Tuple[float, float, float]]) -> float:
    if len(points_3d) < 3:
        return 0.0
    hull_2d = _convex_hull_2d([(p[0], p[1]) for p in points_3d])
    if len(hull_2d) < 3:
        return 0.0
    area_2d = _shoelace_area_2d(hull_2d)
    hull_3d = []
    for hx, hy in hull_2d:
        for px, py, pz in points_3d:
            if math.isclose(px, hx, abs_tol=1e-09) and math.isclose(py, hy, abs_tol=1e-09):
                hull_3d.append((px, py, pz))
                break
    if len(hull_3d) < 3:
        return 0.0
    total_area = 0.0
    origin = (0.0, 0.0, 0.0)
    n = len(hull_3d)
    for i in range(n):
        p1 = hull_3d[i]
        p2 = hull_3d[(i + 1) % n]
        cp_x = p1[1] * p2[2] - p1[2] * p2[1]
        cp_y = p1[2] * p2[0] - p1[0] * p2[2]
        cp_z = p1[0] * p2[1] - p1[1] * p2[0]
        mag_cross = math.sqrt(cp_x ** 2 + cp_y ** 2 + cp_z ** 2)
        mag_p1 = math.sqrt(p1[0] ** 2 + p1[1] ** 2 + p1[2] ** 2)
        mag_p2 = math.sqrt(p2[0] ** 2 + p2[1] ** 2 + p2[2] ** 2)
        if mag_cross == 0 or mag_p1 == 0 or mag_p2 == 0:
            continue
        sin_angle = mag_cross / (mag_p1 * mag_p2)
        cos_angle = (p1[0] * p2[0] + p1[1] * p2[1] + p1[2] * p2[2]) / (mag_p1 * mag_p2)
        sin_angle = max(-1.0, min(1.0, sin_angle))
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle = math.atan2(sin_angle, cos_angle)
        total_area += angle
    total_cross_z = 0.0
    total_dot = 0.0
    for i in range(n):
        p1 = hull_3d[i]
        p2 = hull_3d[(i + 1) % n]
        cross_x = p1[1] * p2[2] - p1[2] * p2[1]
        cross_y = p1[2] * p2[0] - p1[0] * p2[2]
        cross_z = p1[0] * p2[1] - p1[1] * p2[0]
        total_cross_z += cross_z
        total_dot += p1[0] * p2[0] + p1[1] * p2[1] + p1[2] * p2[2]
    ref = hull_3d[0]
    poly_area = 0.0
    for i in range(1, n - 1):
        p1 = hull_3d[i]
        p2 = hull_3d[i + 1]
        cross_product = (p1[1] * p2[2] - p1[2] * p2[1], p1[2] * p2[0] - p1[0] * p2[2], p1[0] * p2[1] - p1[1] * p2[0])
        det = ref[0] * cross_product[0] + ref[1] * cross_product[1] + ref[2] * cross_product[2]
        dot01 = ref[0] * p1[0] + ref[1] * p1[1] + ref[2] * p1[2]
        dot12 = p1[0] * p2[0] + p1[1] * p2[1] + p1[2] * p2[2]
        dot20 = p2[0] * ref[0] + p2[1] * ref[1] + p2[2] * ref[2]
        denom = 1.0 + dot01 + dot12 + dot20
        if denom == 0:
            continue
        angle = 2.0 * math.atan2(abs(det), denom)
        poly_area += angle
    return poly_area

def calculate_convex_hull_area(lat_lon_points: List[Tuple[float, float]]) -> float:
    if not lat_lon_points:
        return 0.0
    points_3d = [_to_cartesian(lat, lon) for lat, lon in lat_lon_points]
    return _compute_3d_convex_hull_area(points_3d)
if __name__ == '__main__':
    sample_coords = [(40.7128, -74.006), (34.0522, -118.2437), (41.8781, -87.6298), (29.7604, -95.3698), (33.4484, -112.074)]
    area = calculate_convex_hull_area(sample_coords)
    print(area)