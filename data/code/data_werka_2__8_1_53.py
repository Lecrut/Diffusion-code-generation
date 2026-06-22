import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        raise ValueError('The list of coordinates cannot be empty.')
    coords_array = np.array(coordinates)
    min_x, max_x = (np.min(coords_array[:, 0]), np.max(coords_array[:, 0]))
    min_y, max_y = (np.min(coords_array[:, 1]), np.max(coords_array[:, 1]))
    width = max_x - min_x
    height = max_y - min_y
    area = width * height
    return area
if __name__ == '__main__':
    sample_coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
    area = calculate_smallest_bounding_box_area(sample_coordinates)
    print(area)