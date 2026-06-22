import numpy as np

def area_difference(region1, region2):
    xor_result = np.bitwise_xor(region1, region2)
    difference_count = np.sum(xor_result)
    return difference_count
if __name__ == '__main__':
    region1 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    region2 = np.array([[0, 0, 0], [1, 0, 1], [0, 1, 0]])
    result = area_difference(region1, region2)
    print(result)