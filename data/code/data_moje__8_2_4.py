import numpy as np

def bounding_box_area(coordinates):
    if not coordinates:
        return 0
    points = np.array(coordinates)
    min_x = np.min(points[:, 0])
    max_x = np.max(points[:, 0])
    min_y = np.min(points[:, 1])
    max_y = np.max(points[:, 1])
    width = max_x - min_x
    height = max_y - min_y
    return float(width * height)

if __name__ == '__main__':
    sample_coords = [(0, 0), (10, 0), (10, 10), (0, 10)]
    area = bounding_box_area(sample_coords)
    print(area)