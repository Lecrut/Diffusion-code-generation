import numpy as np

def validate_regions(region1, region2):
    if region1.shape != region2.shape:
        raise ValueError('Both regions must have the same shape.')
    if not np.issubdtype(region1.dtype, np.bool_) or not np.issubdtype(region2.dtype, np.bool_):
        raise ValueError('Both regions must be binary matrices (numpy arrays of dtype bool).')

def area_difference(region1, region2):
    validate_regions(region1, region2)
    xor_result = np.bitwise_xor(region1, region2)
    return np.sum(xor_result)

if __name__ == '__main__':
    region1 = np.array([[True, False, True], [False, True, False], [True, False, True]])
    region2 = np.array([[False, True, False], [True, False, True], [False, True, False]])
    difference = area_difference(region1, region2)
    print(difference)