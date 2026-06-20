import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        return 0.0
    points = np.array(coordinates)
    if points.ndim != 2 or points.shape[1] < 2:
        raise ValueError("Coordinates must be a list of (x, y) tuples")
    min_x = np.min(points[:, 0])
    max_x = np.max(points[:, 0])
    min_y = np.min(points[:, 1])
    max_y = np.max(points[:, 1])
    width = max_x - min_x
    height = max_y - min_y
    return width * height

if __name__ == '__main__':
    sample_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3), (2, 1)]
    result = calculate_smallest_bounding_box_area(sample_coordinates)
    print(result)