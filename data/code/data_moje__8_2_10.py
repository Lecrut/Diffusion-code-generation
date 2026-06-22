import numpy as np

def calculate_bounding_box_area(coordinates):
    if not coordinates:
        return 0.0
    points = np.array(coordinates)
    min_coords = np.min(points, axis=0)
    max_coords = np.max(points, axis=0)
    if np.any(min_coords == max_coords):
        return 0.0
    widths = max_coords - min_coords
    return float(np.prod(widths))

if __name__ == '__main__':
    sample_coordinates = [(1, 2), (3, 5), (6, 8), (4, 3)]
    result = calculate_bounding_box_area(sample_coordinates)
    print(result)