import numpy as np

def area_difference(region1, region2):
    if not np.issubdtype(region1.dtype, np.bool_) or not np.issubdtype(region2.dtype, np.bool_):
        raise ValueError('Both regions must be binary matrices (numpy arrays of dtype bool).')
    area1 = np.sum(region1)
    area2 = np.sum(region2)
    return abs(area1 - area2)
if __name__ == '__main__':
    region1 = np.array([[True, False, True], [False, True, False], [True, False, True]])
    region2 = np.array([[False, True, False], [True, False, True], [False, True, False]])
    difference = area_difference(region1, region2)
    print(difference)