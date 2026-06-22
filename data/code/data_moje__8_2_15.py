import numpy as np

def calculate_smallest_bounding_box_area(points):
    if not points:
        return 0.0
    array_points = np.array(points)
    if array_points.shape[0] == 0:
        return 0.0
    min_x = np.min(array_points[:, 0])
    max_x = np.max(array_points[:, 0])
    min_y = np.min(array_points[:, 1])
    max_y = np.max(array_points[:, 1])
    width = max_x - min_x
    height = max_y - min_y
    return width * height

if __name__ == '__main__':
    sample_points = [(1.5, 2.0), (3.5, 5.5), (0.0, 1.0), (4.0, 6.0)]
    result = calculate_smallest_bounding_box_area(sample_points)
    print(result)