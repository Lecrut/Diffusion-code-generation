import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        raise ValueError('The list of coordinates cannot be empty.')
    points = np.array(coordinates)
    min_x = np.min(points[:, 0])
    max_x = np.max(points[:, 0])
    min_y = np.min(points[:, 1])
    max_y = np.max(points[:, 1])
    width = max_x - min_x
    height = max_y - min_y
    area = width * height
    return area
if __name__ == '__main__':
    sample_coordinates = [(10, 20), (30, 40), (50, 60), (70, 80)]
    bounding_box_area = calculate_smallest_bounding_box_area(sample_coordinates)
    print(bounding_box_area)