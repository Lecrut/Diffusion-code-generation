import numpy as np

def calculate_bounding_box_area(coordinates):
    if not coordinates:
        return 0.0
    points = np.array(coordinates)
    min_coords = np.min(points, axis=0)
    max_coords = np.max(points, axis=0)
    width = max_coords[0] - min_coords[0]
    height = max_coords[1] - min_coords[1]
    return width * height

if __name__ == '__main__':
    sample_points = [(0, 0), (1, 5), (3, 2), (2, 4), (5, 1)]
    area = calculate_bounding_box_area(sample_points)
    print(area)