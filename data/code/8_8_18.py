import math
import numpy as np

def calculate_convex_hull_area(points):
    if len(points) < 3:
        return 0.0

    points_array = np.array(points, dtype=np.float64)
    
    x = points_array[:, 0]
    y = points_array[:, 1]
    
    n = len(x)
    
    area_sum = 0.0
    for i in range(n):
        j = (i + 1) % n
        area_sum += (x[i] * y[j]) - (x[j] * y[i])
    
    return abs(area_sum) / 2.0

def get_convex_hull_area_for_coordinates(points):
    if len(points) < 3:
        return 0.0
    
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    
    n = len(points)
    
    area_sum = 0.0
    for i in range(n):
        j = (i + 1) % n
        area_sum += (x[i] * y[j]) - (x[j] * y[i])
    
    return abs(area_sum) / 2.0

def compute_convex_hull_and_area(points):
    if len(points) < 3:
        return 0.0
    
    n = len(points)
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    
    area_sum = 0.0
    for i in range(n):
        j = (i + 1) % n
        area_sum += (x[i] * y[j]) - (x[j] * y[i])
    
    return abs(area_sum) / 2.0

if __name__ == '__main__':
    sample_coordinates = [
        (0.0, 0.0),
        (10.0, 0.0),
        (10.0, 10.0),
        (0.0, 10.0)
    ]
    
    result_area = compute_convex_hull_and_area(sample_coordinates)
    print(result_area)