import math
from itertools import permutations

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def cross_product_o(a, b, c):
    return (b[1] - a[1]) * (c[2] - a[2]) - (b[2] - a[2]) * (c[1] - a[1])

def convex_hull(points):
    points = sorted(set(points), key=lambda p: (p[0], p[1]))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product_o(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product_o(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def shoelace_area_cartesian(points):
    n = len(points)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

def spherical_convex_hull_area(coords):
    if len(coords) < 3:
        return 0.0
    hull_indices = convex_hull([(c[0], c[1], c[2]) for c in coords])
    R = 6371.0
    total_area = 0.0
    n = len(hull_indices)
    for i in range(n):
        j = (i + 1) % n
        p1 = hull_indices[i]
        p2 = hull_indices[j]
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        cross_x = y1 * z2 - z1 * y2
        cross_y = z1 * x2 - x1 * z2
        cross_z = x1 * y2 - y1 * x2
        edge_normal = (cross_x, cross_y, cross_z)
        edge_len = math.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        if edge_len == 0:
            continue
        theta = math.acos(max(-1, min(1, (x1 * x2 + y1 * y2 + z1 * z2) / (edge_len))))
        total_area += theta * edge_len
    return 0.5 * total_area

def lat_lon_to_cartesian(lat, lon):
    phi = math.radians(90 - lat)
    theta = math.radians(lon + 180)
    x = -math.sin(phi) * math.cos(theta)
    y = math.cos(phi)
    z = math.sin(phi) * math.sin(theta)
    return x, y, z

def calculate_convex_hull_area(coords):
    cart_coords = [lat_lon_to_cartesian(lat, lon) for lat, lon in coords]
    return spherical_convex_hull_area(cart_coords)

if __name__ == '__main__':
    sample_coords = [
        (40.7128, -74.0060),
        (34.0522, -118.2437),
        (41.8781, -87.6298),
        (29.7604, -95.3698),
        (39.7392, -104.9903)
    ]
    result = calculate_convex_hull_area(sample_coords)
    print(result)