import numpy as np

def compare_measurements(arr1, arr2):
    arr1 = np.asarray(arr1)
    arr2 = np.asarray(arr2)
    diff = arr1 - arr2
    signs = np.sign(diff)
    return signs

if __name__ == '__main__':
    measurements_a = np.array([10.5, 20.0, 15.3, 8.8, 0.0])
    measurements_b = np.array([10.0, 20.0, 16.0, 8.8, 5.0])
    result = compare_measurements(measurements_a, measurements_b)
    print(result)