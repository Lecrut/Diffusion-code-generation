import numpy as np

def area_difference(region1: np.ndarray, region2: np.ndarray) -> int:
    if region1.shape != region2.shape:
        raise ValueError('Input regions must have the same shape')
    difference = region1 ^ region2
    return np.sum(difference)
if __name__ == '__main__':
    region1 = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    region2 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    result = area_difference(region1, region2)
    print(result)