import numpy as np

def smallest_bounding_box_area(coordinates):
    if not coordinates:
        return 0.0
    points = np.array(coordinates)
    if points.ndim == 1:
        points = points.reshape(1, -1)
    x_coords = points[:, 0]
    y_coords = points[:, 1]
    width = np.max(x_coords) - np.min(x_coords)
    height = np.max(y_coords) - np.min(y_coords)
    return float(width * height)

if __name__ == '__main__':
    sample_coords = [(0, 0), (3, 0), (3, 4), (0, 4)]
    area = smallest_bounding_box_area(sample_coords)
    print(area)