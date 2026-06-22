import numpy as np

def compare_measurements(arr1, arr2):
    return np.sign(np.subtract(arr1, arr2))

if __name__ == '__main__':
    measurements1 = np.array([10.5, 20.0, 5.0, 15.5])
    measurements2 = np.array([10.5, 19.0, 6.0, 15.5])
    result = compare_measurements(measurements1, measurements2)
    print(result)