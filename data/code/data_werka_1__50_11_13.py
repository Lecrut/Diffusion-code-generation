import numpy as np

def area_difference(region1, region2):
    diff = np.bitwise_xor(region1, region2)
    return np.sum(diff)
if __name__ == '__main__':
    region1 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    region2 = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    result = area_difference(region1, region2)
    print(result)