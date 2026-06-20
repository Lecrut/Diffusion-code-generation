import math
from scipy.spatial import ConvexHull

def convex_hull_area_ll(lat_lon_list):
    if len(lat_lon_list) < 3:
        return 0.0
    
    lats = [p[0] for p in lat_lon_list]
    lons = [p[1] for p in lat_lon_list]
    
    lat_rad = [math.radians(lat) for lat in lats]
    lon_rad = [math.radians(lon) for lon in lons]
    
    x = [math.cos(lat) * math.cos(lon) for lat, lon in zip(lat_rad, lon_rad)]
    y = [math.cos(lat) * math.sin(lon) for lat, lon in zip(lat_rad, lon_rad)]
    z = [math.sin(lat) for lat in lat_rad]
    
    points_3d = list(zip(x, y, z))
    
    hull = ConvexHull(points_3d)
    
    total_area = 0.0
    for simplex in hull.simplices:
        p1 = points_3d[simplex[0]]
        p2 = points_3d[simplex[1]]
        p3 = points_3d[simplex[2]]
        
        v1 = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
        v2 = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
        
        cross_x = v1[1] * v2[2] - v1[2] * v2[1]
        cross_y = v1[2] * v2[0] - v1[0] * v2[2]
        cross_z = v1[0] * v2[1] - v1[1] * v2[0]
        
        mag = math.sqrt(cross_x**2 + cross_y**2 + cross_z**2)
        total_area += mag
    
    return total_area

if __name__ == '__main__':
    sample_coords = [
        (40.0, -105.0),
        (41.0, -104.0),
        (40.0, -103.0),
        (39.0, -104.0),
    ]
    area = convex_hull_area_ll(sample_coords)
    print(area)