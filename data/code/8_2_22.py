import numpy as np

def calculate_smallest_bounding_box_area(points):
    if not points:
        return 0
    points_array = np.array(points)
    min_x = np.min(points_array[:, 0])
    max_x = np.max(points_array[:, 0])
    min_y = np.min(points_array[:, 1])
    max_y = np.max(points_array[:, 1])
    width = max_x - min_x
    height = max_y - min_y
    return width * height
if __name__ == '__main__':
    sample_points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    area = calculate_smallest_bounding_box_area(sample_points)
    print(area)