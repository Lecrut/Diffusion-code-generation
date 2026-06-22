import numpy as np

def compare_measurements(arr1, arr2):
    a = np.asarray(arr1, dtype=np.float64)
    b = np.asarray(arr2, dtype=np.float64)
    diff = a - b
    return np.where(diff > 0, 1, np.where(diff < 0, -1, 0))

if __name__ == '__main__':
    measurements1 = [10.5, 20.0, 15.3, 8.1]
    measurements2 = [10.5, 15.0, 15.3, 12.1]
    result = compare_measurements(measurements1, measurements2)
    print(result)