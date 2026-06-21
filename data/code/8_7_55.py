import numpy as np

def calculate_convex_hull_area(coordinates):
    sorted_coords = sorted(coordinates, key=lambda x: (x[0], x[1]))
    points = np.array(sorted_coords)
    n = len(points)
    area = 0.5 * abs(np.dot(points[:, 0], np.roll(points[:, 1], 1)) - np.dot(points[:, 1], np.roll(points[:, 0], 1)))
    return area
if __name__ == '__main__':
    sample_coords = [(34.0522, -118.2437), (40.7128, -74.006), (37.7749, -122.4194), (47.6062, -122.3321)]
    area = calculate_convex_hull_area(sample_coords)
    print(area)