import numpy as np

def smallest_bounding_box_area(points):
    if not points:
        return 0.0
    points_array = np.array(points)
    min_coords = np.min(points_array, axis=0)
    max_coords = np.max(points_array, axis=0)
    width = max_coords[0] - min_coords[0]
    height = max_coords[1] - min_coords[1]
    return width * height

if __name__ == '__main__':
    sample_points = [(1, 2), (3, 4), (0, 0), (5, 1)]
    result = smallest_bounding_box_area(sample_points)
    print(result)