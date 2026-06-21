import numpy as np

def area_difference(region1, region2):
    if not isinstance(region1, np.ndarray) or not isinstance(region2, np.ndarray):
        raise ValueError('Both regions must be numpy arrays.')
    if region1.shape != region2.shape:
        raise ValueError('Both regions must have the same shape.')
    xor_result = np.bitwise_xor(region1, region2)
    return np.sum(xor_result)

if __name__ == '__main__':
    region1 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    region2 = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    difference = area_difference(region1, region2)
    print(difference)