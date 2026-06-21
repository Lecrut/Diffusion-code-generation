import numpy as np

def area_difference(region1, region2):
    region1 = np.array(region1, dtype=bool)
    region2 = np.array(region2, dtype=bool)
    difference = np.bitwise_xor(region1, region2)
    return np.sum(difference)
if __name__ == '__main__':
    region1 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    region2 = [[0, 0, 0], [1, 0, 1], [0, 1, 0]]
    result = area_difference(region1, region2)
    print(result)