import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        raise ValueError('The list of coordinates cannot be empty.')
    coords = np.array(coordinates)
    min_x, max_x = (np.min(coords[:, 0]), np.max(coords[:, 0]))
    min_y, max_y = (np.min(coords[:, 1]), np.max(coords[:, 1]))
    width = max_x - min_x
    height = max_y - min_y
    return width * height
if __name__ == '__main__':
    sample_coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
    area = calculate_smallest_bounding_box_area(sample_coordinates)
    print(area)