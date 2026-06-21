import numpy as np
MIN_DIMENSION = 0

def calculate_smallest_bounding_box_area(coordinates):
    if not coordinates:
        raise ValueError('The list of coordinates cannot be empty.')
    points = np.array(coordinates)
    x_min, x_max = (np.min(points[:, 0]), np.max(points[:, 0]))
    y_min, y_max = (np.min(points[:, 1]), np.max(points[:, 1]))
    width = x_max - x_min
    height = y_max - y_min
    if width < MIN_DIMENSION or height < MIN_DIMENSION:
        raise ValueError('Invalid coordinates: bounding box dimensions cannot be negative.')
    area = width * height
    return area
if __name__ == '__main__':
    sample_coordinates = [(10, 20), (30, 40), (50, 60), (70, 80)]
    try:
        area = calculate_smallest_bounding_box_area(sample_coordinates)
        print(area)
    except ValueError as e:
        print(e)