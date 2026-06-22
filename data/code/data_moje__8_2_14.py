import numpy as np

def bounding_box_area(points):
    if not points:
        return 0
    coords = np.array(points)
    min_x, min_y = np.min(coords, axis=0)
    max_x, max_y = np.max(coords, axis=0)
    width = max_x - min_x
    height = max_y - min_y
    return width * height

if __name__ == '__main__':
    points = [(1, 1), (4, 1), (4, 5), (1, 5), (2, 3)]
    result = bounding_box_area(points)
    print(result)