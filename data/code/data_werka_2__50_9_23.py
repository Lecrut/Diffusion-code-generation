import numpy as np

def area_difference(region1, region2):
    region1 = np.array(region1)
    region2 = np.array(region2)
    xor_result = np.bitwise_xor(region1, region2)
    return np.sum(xor_result)
if __name__ == '__main__':
    region1 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    region2 = [[1, 1, 0], [1, 0, 1], [0, 1, 0]]
    difference = area_difference(region1, region2)
    print(difference)