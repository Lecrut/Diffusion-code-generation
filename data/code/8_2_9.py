import numpy as np

def bounding_box_area(points):
    arr = np.array(points)
    min_x = np.min(arr[:, 0])
    max_x = np.max(arr[:, 0])
    min_y = np.min(arr[:, 1])
    max_y = np.max(arr[:, 1])
    width = max_x - min_x
    height = max_y - min_y
    return float(width * height)

if __name__ == '__main__':
    coords = [(1, 1), (3, 1), (3, 4), (1, 4)]
    area = bounding_box_area(coords)
    print(area)