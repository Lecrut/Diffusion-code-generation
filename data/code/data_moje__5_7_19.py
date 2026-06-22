import numpy as np

def compare_length_measurements(arr1, arr2):
    a1 = np.asarray(arr1, dtype=np.float64)
    a2 = np.asarray(arr2, dtype=np.float64)
    diff = a1 - a2
    result = np.where(diff > 0, 1, np.where(diff < 0, -1, 0))
    return result

if __name__ == '__main__':
    lengths1 = [10.5, 20.0, 15.5, 15.5, 10.0]
    lengths2 = [10.0, 20.5, 15.5, 16.0, 10.0]
    result = compare_length_measurements(lengths1, lengths2)
    print(result)