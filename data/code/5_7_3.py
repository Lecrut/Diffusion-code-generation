import numpy as np

def compare_measurements(measurements1, measurements2):
    arr1 = np.asarray(measurements1, dtype=np.float64)
    arr2 = np.asarray(measurements2, dtype=np.float64)
    diff = arr1 - arr2
    result = np.zeros_like(diff, dtype=int)
    result[diff > 0] = 1
    result[diff < 0] = -1
    return result

if __name__ == '__main__':
    m1 = [1.5, 2.0, 3.0, 4.5]
    m2 = [1.5, 1.0, 3.5, 4.0]
    print(compare_measurements(m1, m2))