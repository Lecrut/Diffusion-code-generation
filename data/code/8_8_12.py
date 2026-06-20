import math
from itertools import combinations

def convex_hull_graham(points):
    if len(points) < 3:
        return points
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    def dist_sq(a, b):
        return (a[0] - b[0])**2 + (a[1] - b[1])**2
    p0 = min(points)
    remaining = [p for p in points if p != p0]
    def polar_angle_key(p):
        dx, dy = p[0] - p0[0], p[1] - p0[1]
        if dx == 0 and dy == 0:
            return (math.pi, 0)
        angle = math.atan2(dy, dx)
        if angle < 0:
            angle += 2 * math.pi
        return (angle, dist_sq(p0, p))
    remaining.sort(key=polar_angle_key)
    hull = [p0]
    for p in remaining:
        while len(hull) > 1 and cross(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull

def shoelace_area(hull_points):
    n = len(hull_points)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += hull_points[i][0] * hull_points[j][1]
        area -= hull_points[j][0] * hull_points[i][1]
    return abs(area) / 2.0

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def estimate_earth_area_ratio(hull_points):
    if len(hull_points) < 3:
        return 0.0
    total_area = 0.0
    n = len(hull_points)
    for i in range(1, n - 1):
        dist1 = haversine_distance(hull_points[0][0], hull_points[0][1], hull_points[i][0], hull_points[i][1])
        dist2 = haversine_distance(hull_points[i][0], hull_points[i][1], hull_points[i+1][0], hull_points[i+1][1])
        angle_i = math.radians(hull_points[i][1] - hull_points[0][1])
        approx_area = 0.5 * dist1 * dist2 * math.sin(angle_i)
        total_area += abs(approx_area)
    return total_area

def convex_hull_area(coords):
    hull = convex_hull_graham(coords)
    return shoelace_area(hull)

if __name__ == '__main__':
    sample_coords = [
        (52.5200, 13.4050),
        (48.8566, 2.3522),
        (51.5074, -0.1278),
        (41.9028, 12.4964),
        (34.0522, -118.2437),
        (37.7749, -122.4194),
        (35.6895, 139.6917),
        (31.2304, 121.4737)
    ]
    area = convex_hull_area(sample_coords)
    print(area)