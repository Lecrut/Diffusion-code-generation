import numpy as np

def compare_signs(array1, array2):
    array1 = np.asarray(array1)
    array2 = np.asarray(array2)
    diff = array1 - array2
    result = np.sign(diff)
    return result

if __name__ == '__main__':
    measurements_a = np.array([10.5, 20.0, 15.5, 8.0, 12.0])
    measurements_b = np.array([10.0, 20.0, 16.0, 5.0, 12.0])
    signs = compare_signs(measurements_a, measurements_b)
    print(signs)