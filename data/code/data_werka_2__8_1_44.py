import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        raise ValueError('The list of coordinates cannot be empty.')
    coords = np.array(coordinates)
    min_x, min_y = coords.min(axis=0)
    max_x, max_y = coords.max(axis=0)
    width = max_x - min_x
    height = max_y - min_y
    area = width * height
    return area
if __name__ == '__main__':
    sample_coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
    area = calculate_smallest_bounding_box_area(sample_coordinates)
    print(area)