import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        return 0
    points = np.array(coordinates)
    min_x, min_y = np.min(points, axis=0)
    max_x, max_y = np.max(points, axis=0)
    width = max_x - min_x
    height = max_y - min_y
    area = width * height
    return area
if __name__ == '__main__':
    sample_coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
    print(calculate_smallest_bounding_box_area(sample_coordinates))