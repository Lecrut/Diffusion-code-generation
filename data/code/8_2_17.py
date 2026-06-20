import numpy as np

def calculate_smallest_bounding_box_area(points):
    if not points:
        return 0.0
    array_points = np.array(points)
    x_min = np.min(array_points[:, 0])
    x_max = np.max(array_points[:, 0])
    y_min = np.min(array_points[:, 1])
    y_max = np.max(array_points[:, 1])
    width = x_max - x_min
    height = y_max - y_min
    return width * height

if __name__ == '__main__':
    sample_points = [(1, 2), (3, 5), (0, 1), (4, 6), (2, 2)]
    result = calculate_smallest_bounding_box_area(sample_points)
    print(result)