import math

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.01
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def convex_hull_graham(points):
    if len(points) < 3:
        return list(points)
    
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    def dist_sq(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    
    lowest = min(points, key=lambda p: (p[1], p[0]))
    remaining = [p for p in points if p != lowest or p is lowest]
    remaining.remove(lowest)
    
    def polar_angle_key(p):
        angle = math.atan2(p[1] - lowest[1], p[0] - lowest[0])
        if angle < 0:
            angle += 2 * math.pi
        return (angle, dist_sq(lowest, p))
    
    remaining.sort(key=polar_angle_key)
    
    stack = [lowest]
    for p in remaining:
        while len(stack) > 1 and cross(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)
    
    if len(stack) == len(points) and len(points) > 2:
        if cross(stack[0], stack[1], stack[-1]) < 0:
            stack = stack[::-1]
    
    return stack

def shoelace_area(points):
    n = len(points)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

def area_on_sphere(points):
    n = len(points)
    if n < 3:
        return 0.0
    
    R = 6371.01
    
    latlons = [(math.radians(p[0]), math.radians(p[1])) for p in points]
    
    def cross_product(a, b):
        x = a[1] * b[2] - a[2] * b[1]
        y = a[2] * b[0] - a[0] * b[2]
        z = a[0] * b[1] - a[1] * b[0]
        return (x, y, z)
    
    def normalize(v):
        mag = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
        if mag == 0:
            return (0, 0, 0)
        return (v[0]/mag, v[1]/mag, v[2]/mag)
    
    def spherical_excess_area(points_3d):
        total_excess = 0.0
        for i in range(len(points_3d)):
            j = (i + 1) % len(points_3d)
            v1 = points_3d[i]
            v2 = points_3d[j]
            cross_v = cross_product(v1, v2)
            a = math.atan2(math.sqrt(cross_v[0]**2 + cross_v[1]**2 + cross_v[2]**2), v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2])
            total_excess += a
        
        area = R * R * total_excess
        return area
    
    def to_3d(lat, lon):
        x = math.cos(lat) * math.cos(lon)
        y = math.cos(lat) * math.sin(lon)
        z = math.sin(lat)
        return (x, y, z)
    
    points_3d = [to_3d(lat, lon) for lat, lon in latlons]
    
    return spherical_excess_area(points_3d)

def calculate_convex_hull_area(coords):
    if len(coords) < 3:
        return 0.0
    
    hull = convex_hull_graham(coords)
    
    return area_on_sphere(hull)

if __name__ == '__main__':
    sample_coords = [
        (40.7128, -74.0060),
        (34.0522, -118.2437),
        (41.8781, -87.6298),
        (29.7604, -95.3698),
        (47.6062, -122.3321),
        (39.9526, -75.1652),
        (32.7767, -96.7970),
        (36.1627, -86.7816),
        (33.4484, -112.0740),
        (35.2271, -80.8431)
    ]
    
    result = calculate_convex_hull_area(sample_coords)
    print(result)