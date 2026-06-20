import math

def calculate_convex_hull_area(points):
    n = len(points)
    if n < 3:
        return 0.0
    
    sorted_points = sorted(points)
    hull = []
    
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    k = 0
    for p in sorted_points:
        while k >= 2 and cross_product(hull[k-2], hull[k-1], p) <= 0:
            hull.pop()
            k -= 1
        hull.append(p)
        k += 1
    
    t = k + 1
    for i in range(n - 2, -1, -1):
        p = sorted_points[i]
        while k >= t and cross_product(hull[k-2], hull[k-1], p) <= 0:
            hull.pop()
            k -= 1
        hull.append(p)
        k += 1
    
    hull.pop()
    
    total = 0.0
    m = len(hull)
    for i in range(m):
        j = (i + 1) % m
        total += hull[i][0] * hull[j][1]
        total -= hull[j][0] * hull[i][1]
    
    return abs(total) / 2.0

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c

def spherical_to_cartesian(lat, lon):
    phi = math.radians(lat)
    theta = math.radians(lon)
    x = math.cos(phi) * math.cos(theta)
    y = math.cos(phi) * math.sin(theta)
    z = math.sin(phi)
    return (x, y, z)

def convex_hull_3d(points_3d):
    n = len(points_3d)
    if n < 3:
        return points_3d
    
    indices = list(range(n))
    indices.sort(key=lambda i: points_3d[i][0])
    
    hull = []
    
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    k = 0
    for i in indices:
        p = points_3d[i]
        while k >= 2 and cross_product(hull[k-2], hull[k-1], p) <= 0:
            hull.pop()
            k -= 1
        hull.append(p)
        k += 1
    
    t = k + 1
    for i in range(n - 2, -1, -1):
        p = points_3d[indices[i]]
        while k >= t and cross_product(hull[k-2], hull[k-1], p) <= 0:
            hull.pop()
            k -= 1
        hull.append(p)
        k += 1
    
    hull.pop()
    return hull

def calculate_spherical_convex_hull_area(points):
    n = len(points)
    if n < 3:
        return 0.0
    
    if n == 3:
        lat1, lon1 = points[0]
        lat2, lon2 = points[1]
        lat3, lon3 = points[2]
        a = haversine_distance(lat1, lon1, lat2, lon2)
        b = haversine_distance(lat2, lon2, lat3, lon3)
        c = haversine_distance(lat3, lon3, lat1, lon1)
        s = (a + b + c) / 2
        if s <= 0 or s - a <= 0 or s - b <= 0 or s - c <= 0:
            return 0.0
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area * 1e6
    
    cartesian_points = [spherical_to_cartesian(lat, lon) for lat, lon in points]
    hull_cartesian = convex_hull_3d(cartesian_points)
    
    total_area = 0.0
    m = len(hull_cartesian)
    if m < 3:
        return 0.0
    
    center = [0.0, 0.0, 0.0]
    for p in hull_cartesian:
        center[0] += p[0]
        center[1] += p[1]
        center[2] += p[2]
    center[0] /= m
    center[1] /= m
    center[2] /= m
    
    for i in range(m):
        j = (i + 1) % m
        p1 = hull_cartesian[i]
        p2 = hull_cartesian[j]
        
        a_len = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
        b_len = math.sqrt(p2[0]**2 + p2[1]**2 + p2[2]**2)
        c_vec = (p1[1] * p2[2] - p1[2] * p2[1], p1[2] * p2[0] - p1[0] * p2[2], p1[0] * p2[1] - p1[1] * p2[0])
        c_len = math.sqrt(c_vec[0]**2 + c_vec[1]**2 + c_vec[2]**2)
        
        if c_len == 0:
            continue
        
        dot_a = p1[0] * p2[0] + p1[1] * p2[1] + p1[2] * p2[2]
        cos_angle = dot_a / (a_len * b_len)
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle = math.acos(cos_angle)
        
        area = 0.5 * a_len * b_len * math.sin(angle)
        total_area += area
    
    return total_area * (6371000**2)

if __name__ == '__main__':
    sample_points = [
        (40.0, -74.0),
        (41.0, -73.0),
        (42.0, -75.0),
        (39.0, -76.0),
        (38.0, -72.0)
    ]
    area = calculate_spherical_convex_hull_area(sample_points)
    print(area)