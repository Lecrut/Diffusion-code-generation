import numpy as np

def area_difference(region1, region2):
    region1 = np.array(region1)
    region2 = np.array(region2)
    if region1.shape != region2.shape:
        raise ValueError('Both regions must have the same dimensions.')
    union = np.bitwise_or(region1, region2)
    intersection = np.bitwise_and(region1, region2)
    difference = np.sum(union) - np.sum(intersection)
    return difference
if __name__ == '__main__':
    region1 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    region2 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    result = area_difference(region1, region2)
    print(result)