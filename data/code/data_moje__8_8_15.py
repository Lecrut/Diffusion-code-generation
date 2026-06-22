import math

def calculate_convex_hull_area(points):
    if len(points) < 3:
        return 0.0
    
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    sorted_points = sorted(points)
    
    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    hull = lower[:-1] + upper[:-1]
    
    if len(hull) < 3:
        return 0.0
    
    area = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    
    return abs(area) / 2.0

def radians_to_degrees(radians):
    return radians * 180.0 / math.pi

def degrees_to_radians(degrees):
    return degrees * math.pi / 180.0

def calculate_convex_hull_area_geo(points):
    if len(points) < 3:
        return 0.0
    
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    sorted_points = sorted(points)
    
    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    hull = lower[:-1] + upper[:-1]
    
    if len(hull) < 3:
        return 0.0
    
    earth_radius_km = 6371.0
    n = len(hull)
    total_area = 0.0
    
    for i in range(n):
        j = (i + 1) % n
        
        lat1_rad = degrees_to_radians(hull[i][0])
        lon1_rad = degrees_to_radians(hull[i][1])
        lat2_rad = degrees_to_radians(hull[j][0])
        lon2_rad = degrees_to_radians(hull[j][1])
        
        d_lon = lon2_rad - lon1_rad
        
        area_segment = 2 * math.atan2(
            math.tan(lat2_rad - lat1_rad / 2) * math.sin(d_lon / 2) * 
            math.sin(lat1_rad + lat2_rad) * math.sin(lat1_rad + lat2_rad),
            1 + math.cos(lat1_rad) * math.cos(lat2_rad) + math.sin(lat1_rad) * math.sin(lat2_rad) * math.cos(d_lon)
        )
        
        total_area += area_segment
    
    return total_area * earth_radius_km * earth_radius_km / 2

def calculate_convex_hull_area_planar(points):
    if len(points) < 3:
        return 0.0
    
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    sorted_points = sorted(points)
    
    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    hull = lower[:-1] + upper[:-1]
    
    if len(hull) < 3:
        return 0.0
    
    area = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    
    return abs(area) / 2.0

def calculate_total_area(points, unit='planar'):
    if unit == 'geo':
        return calculate_convex_hull_area_geo(points)
    else:
        return calculate_convex_hull_area_planar(points)

if __name__ == '__main__':
    sample_coordinates = [
        (40.7128, -74.0060),
        (34.0522, -118.2437),
        (41.8781, -87.6298),
        (29.7604, -95.3698),
        (39.7392, -104.9903)
    ]
    
    planar_area = calculate_total_area(sample_coordinates, unit='planar')
    print(planar_area)
    
    geo_area = calculate_total_area(sample_coordinates, unit='geo')
    print(geo_area)