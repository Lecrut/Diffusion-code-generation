import numpy as np

def smallest_bounding_box_area(coordinates):
    if not coordinates:
        return 0.0
    coords_array = np.array(coordinates)
    x_min = np.min(coords_array[:, 0])
    x_max = np.max(coords_array[:, 0])
    y_min = np.min(coords_array[:, 1])
    y_max = np.max(coords_array[:, 1])
    width = x_max - x_min
    height = y_max - y_min
    return float(width * height)

if __name__ == '__main__':
    sample_coords = [(1, 2), (3, 4), (5, 1), (2, 5)]
    area = smallest_bounding_box_area(sample_coords)
    print(area)