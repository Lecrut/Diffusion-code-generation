import numpy as np

def calculate_bounding_box_area(coordinates):
    if not coordinates:
        return 0.0
    points = np.array(coordinates)
    if points.ndim != 2 or points.shape[1] < 2:
        raise ValueError("Coordinates must be a list of (x, y) tuples")
    min_x, min_y = np.min(points, axis=0)
    max_x, max_y = np.max(points, axis=0)
    width = max_x - min_x
    height = max_y - min_y
    return float(width * height)

if __name__ == '__main__':
    sample_coordinates = [(1, 1), (5, 2), (3, 4), (4, 1)]
    area = calculate_bounding_box_area(sample_coordinates)
    print(area)