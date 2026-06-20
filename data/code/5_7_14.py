import numpy as np

def sign_of_difference(arr1, arr2):
    return np.sign(arr1 - arr2)
if __name__ == '__main__':
    lengths1 = np.array([10.5, 15.0, 20.3, 25.7, 30.0])
    lengths2 = np.array([12.0, 14.5, 20.3, 24.0, 31.5])
    result = sign_of_difference(lengths1, lengths2)
    print(result)