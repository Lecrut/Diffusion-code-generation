import numpy as np

def calculate_smallest_bounding_box_area(points):
    if not points:
        return 0.0
    coordinates = np.array(points)
    min_x = np.min(coordinates[:, 0])
    max_x = np.max(coordinates[:, 0])
    min_y = np.min(coordinates[:, 1])
    max_y = np.max(coordinates[:, 1])
    width = max_x - min_x
    height = max_y - min_y
    return width * height

if __name__ == '__main__':
    sample_points = [(1, 1), (3, 1), (3, 3), (1, 3), (2, 2)]
    area = calculate_smallest_bounding_box_area(sample_points)
    print(area)