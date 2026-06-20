import math

def calculate_convex_hull_area(coordinates):
    if len(coordinates) < 3:
        return 0.0
    
    n = len(coordinates)
    points = sorted(set(coordinates), key=lambda x: (x[0], x[1]))
    
    if len(points) < 3:
        return 0.0
    
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
    
    convex_hull = lower[:-1] + upper[:-1]
    hull_n = len(convex_hull)
    
    if hull_n < 3:
        return 0.0
    
    def haversine_area(poly):
        m = len(poly)
        area = 0.0
        for i in range(m):
            j = (i + 1) % m
            area += poly[i][0] * poly[j][1]
            area -= poly[j][0] * poly[i][1]
        return 0.5 * abs(area)
    
    def spherical_shoelace(poly):
        m = len(poly)
        sum_val = 0.0
        for i in range(m):
            j = (i + 1) % m
            lat1 = math.radians(poly[i][0])
            lon1 = math.radians(poly[i][1])
            lat2 = math.radians(poly[j][0])
            lon2 = math.radians(poly[j][1])
            
            term = math.sin(lat1) * math.sin(lat2)
            term += math.cos(lat1) * math.cos(lat2) * math.sin(lon2 - lon1)
            term *= math.cos(lat1) * math.sin(lat2) * math.sin(lon2 - lon1)
            
            sum_val += math.atan2(term, math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1) + math.sin(lat1) * math.sin(lat2))
        
        return abs(sum_val)
    
    if hull_n > 50:
        projected_points = []
        center_lat = sum(p[0] for p in convex_hull) / hull_n
        center_lon = sum(p[1] for p in convex_hull) / hull_n
        
        cos_c = math.cos(math.radians(center_lat))
        R = 6371000.0
        
        for lat, lon in convex_hull:
            dlat = math.radians(lat - center_lat)
            dlon = math.radians(lon - center_lon)
            x = R * dlon * cos_c
            y = R * dlat
            projected_points.append((x, y))
        
        return haversine_area(projected_points)
    else:
        return spherical_shoelace(convex_hull) * (6371000.0 ** 2)

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

if __name__ == '__main__':
    sample_coords = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298), (29.7604, -95.3698)]
    result = calculate_convex_hull_area(sample_coords)
    print(f"{result:.2f}")