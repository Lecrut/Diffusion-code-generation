import numpy as np

def calculate_bounding_box_area(points):
    if not points:
        return 0.0
    arr = np.array(points)
    if arr.size == 0:
        return 0.0
    min_coords = np.min(arr, axis=0)
    max_coords = np.max(arr, axis=0)
    width = max_coords[0] - min_coords[0]
    height = max_coords[1] - min_coords[1]
    return width * height

if __name__ == '__main__':
    sample_points = [(1.0, 2.0), (5.0, 8.0), (3.0, 4.0), (1.0, 8.0)]
    result = calculate_bounding_box_area(sample_points)
    print(result)