import numpy as np

def area_difference(region1, region2):
    xor_result = np.bitwise_xor(region1, region2)
    return np.sum(xor_result)
if __name__ == '__main__':
    region1 = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
    region2 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    difference = area_difference(region1, region2)
    print(difference)