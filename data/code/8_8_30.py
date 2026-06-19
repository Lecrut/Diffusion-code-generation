import numpy as np

def calculate_convex_hull_area(coordinates):
    sorted_coords = sorted(coordinates)
    x = [coord[0] for coord in sorted_coords]
    y = [coord[1] for coord in sorted_coords]
    n = len(x)
    area = 0.5 * abs(sum((x[i] * y[(i + 1) % n] - y[i] * x[(i + 1) % n] for i in range(n))))
    return area
if __name__ == '__main__':
    sample_coords = [(34.0522, -118.2437), (40.7128, -74.006), (37.7749, -122.4194), (47.6062, -122.3321)]
    area = calculate_convex_hull_area(sample_coords)
    print(area)