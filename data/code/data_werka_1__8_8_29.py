import numpy as np

def calculate_convex_hull_area(coordinates):
    points = np.array(coordinates)
    from scipy.spatial import ConvexHull
    hull = ConvexHull(points)
    hull_points = points[hull.vertices]
    n = len(hull_points)
    area = 0.5 * abs(sum((hull_points[i][0] * hull_points[(i + 1) % n][1] - hull_points[(i + 1) % n][0] * hull_points[i][1] for i in range(n))))
    return area
if __name__ == '__main__':
    sample_coordinates = [(34.0522, -118.2437), (40.7128, -74.006), (37.7749, -122.4194), (47.6062, -122.3321)]
    area = calculate_convex_hull_area(sample_coordinates)
    print(area)