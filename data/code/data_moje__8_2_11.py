import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        return 0.0
    points = np.array(coordinates)
    x_min = np.min(points[:, 0])
    x_max = np.max(points[:, 0])
    y_min = np.min(points[:, 1])
    y_max = np.max(points[:, 1])
    width = x_max - x_min
    height = y_max - y_min
    return float(width * height)

if __name__ == '__main__':
    sample_coordinates = [(1, 1), (3, 1), (3, 3), (1, 3)]
    area = calculate_smallest_bounding_box_area(sample_coordinates)
    print(area)