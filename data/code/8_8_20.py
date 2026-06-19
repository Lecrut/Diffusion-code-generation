import numpy as np

def calculate_convex_hull_area(coordinates):
    points = np.array(coordinates)
    sorted_points = points[np.lexsort((points[:, 1], points[:, 0]))]
    n = len(sorted_points)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += sorted_points[i][0] * sorted_points[j][1]
        area -= sorted_points[j][0] * sorted_points[i][1]
    return abs(area) / 2.0
if __name__ == '__main__':
    sample_coordinates = [(34.0522, -118.2437), (40.7128, -74.006), (37.7749, -122.4194), (47.6062, -122.3321)]
    area = calculate_convex_hull_area(sample_coordinates)
    print(area)