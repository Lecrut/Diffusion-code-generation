import numpy as np

def area_difference(region1, region2):
    if region1.shape != region2.shape:
        raise ValueError('Both regions must have the same shape.')
    area1 = np.sum(region1)
    area2 = np.sum(region2)
    return abs(area1 - area2)
if __name__ == '__main__':
    region1 = np.array([[1, 0, 1], [1, 1, 0], [0, 1, 1]])
    region2 = np.array([[0, 1, 0], [1, 0, 1], [1, 1, 0]])
    difference = area_difference(region1, region2)
    print(difference)