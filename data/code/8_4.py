import numpy as np
def calculate_bounding_box_area(points):
    points_array = np.array(points)
    min_x = np.min(points_array[:, 0])
    max_x = np.max(points_array[:, 0])
    min_y = np.min(points_array[:, 1])
    max_y = np.max(points_array[:, 1])
    width = max_x - min_x
    height = max_y - min_y
    area = width * height
    return area
if __name__ == '__main__':
    sample_points = [(1, 5), (3, 1), (7, 8), (2, 3), (5, 6)]
    area = calculate_bounding_box_area(sample_points)
    print(area)