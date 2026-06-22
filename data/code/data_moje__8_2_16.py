import numpy as np

def calculate_bounding_box_area(points):
    if not points:
        return 0.0
    points_array = np.array(points)
    min_x, min_y = np.min(points_array, axis=0)
    max_x, max_y = np.max(points_array, axis=0)
    width = max_x - min_x
    height = max_y - min_y
    return width * height

if __name__ == '__main__':
    sample_points = [(1, 2), (3, 4), (5, 6), (2, 5)]
    area = calculate_bounding_box_area(sample_points)
    print(area)