import numpy as np

def area_difference(region1, region2):
    difference = np.bitwise_xor(region1, region2)
    return np.sum(difference)
if __name__ == '__main__':
    region1 = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    region2 = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
    diff = area_difference(region1, region2)
    print(diff)