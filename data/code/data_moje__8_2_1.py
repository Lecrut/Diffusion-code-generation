import numpy as np

def bounding_box_area(coordinates):
    arr = np.array(coordinates)
    x_min = arr[:, 0].min()
    y_min = arr[:, 1].min()
    x_max = arr[:, 0].max()
    y_max = arr[:, 1].max()
    width = x_max - x_min
    height = y_max - y_min
    if width < 0 or height < 0:
        return 0
    return float(width * height)

if __name__ == '__main__':
    coords = [(0, 0), (1, 1), (2, 3), (4, 2)]
    result = bounding_box_area(coords)
    print(result)