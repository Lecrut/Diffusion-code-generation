import math

def calculate_convex_hull_area(coordinates):
    if len(coordinates) < 3:
        return 0.0

    points = [list(p) for p in coordinates]
    
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    points.sort(key=lambda p: (p[0], p[1]))

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

    hull = lower[:-1] + upper[:-1]

    if len(hull) < 3:
        return 0.0

    def degrees_to_radians(deg):
        return deg * math.pi / 180.0

    def area_on_sphere(hull_points):
        if len(hull_points) < 3:
            return 0.0
        
        total_sum = 0.0
        n = len(hull_points)
        
        for i in range(n):
            j = (i + 1) % n
            p1 = hull_points[i]
            p2 = hull_points[j]
            
            lat1 = degrees_to_radians(p1[0])
            lon1 = degrees_to_radians(p1[1])
            lat2 = degrees_to_radians(p2[0])
            lon2 = degrees_to_radians(p2[1])
            
            cross_val = math.sin(lat2) * math.cos(lat1) * math.sin(lon2 - lon1)
            term = math.atan2(cross_val, math.cos(lat1) * math.cos(lat2) - math.sin(lat1) * math.sin(lat2) * math.cos(lon2 - lon1))
            
            if cross_val == 0:
                term = 0
            
            total_sum += term

        return abs(total_sum) * 6371000 * 6371000 / 2.0

    projected_points = []
    center_lat = sum(p[0] for p in hull) / len(hull)
    center_lon = sum(p[1] for p in hull) / len(hull)
    
    for i in range(len(hull) - 1):
        lat = hull[i][0]
        lon = hull[i][1]
        dist = math.sqrt((lat - center_lat) ** 2 + (lon - center_lon) ** 2)
        if dist < 0.1:
            continue
            
    for p in hull:
        projected_points.append(p)
        
    return area_on_sphere(projected_points)

if __name__ == '__main__':
    sample_coords = [(40.7128, -74.0060), (40.7589, -73.9851), (40.7831, -73.9712), (40.7580, -73.9855), (40.7484, -73.9857)]
    result = calculate_convex_hull_area(sample_coords)
    print(result)