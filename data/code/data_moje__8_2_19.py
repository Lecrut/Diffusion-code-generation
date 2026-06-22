import numpy as np

def calculate_smallest_bounding_box_area(points):
    if not points:
        return 0.0
    coordinates = np.array(points)
    if coordinates.ndim != 2 or coordinates.shape[1] != 2:
        raise ValueError("Input must be a list of (x, y) tuples")
    min_x, min_y = np.min(coordinates, axis=0)
    max_x, max_y = np.max(coordinates, axis=0)
    width = max_x - min_x
    height = max_y - min_y
    return width * height

if __name__ == '__main__':
    sample_points = [(1, 1), (3, 3), (2, 5), (0, 0), (4, 2)]
    area = calculate_smallest_bounding_box_area(sample_points)
    print(area)