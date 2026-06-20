import numpy as np

def calculate_smallest_bounding_box_area(points):
    if not points:
        return 0.0
    points_array = np.array(points)
    min_x, min_y = np.min(points_array, axis=0)
    max_x, max_y = np.max(points_array, axis=0)
    width = max_x - min_x
    height = max_y - min_y
    return float(width * height)

if __name__ == '__main__':
    sample_points = [(0, 0), (1, 1), (2, 3), (4, 0), (5, 5)]
    area = calculate_smallest_bounding_box_area(sample_points)
    print(area)