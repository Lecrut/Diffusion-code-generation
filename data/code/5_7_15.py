import numpy as np

def compare_lengths(a, b):
    arr_a = np.asarray(a, dtype=np.float64)
    arr_b = np.asarray(b, dtype=np.float64)
    diff = arr_a - arr_b
    result = np.sign(diff)
    return result
if __name__ == '__main__':
    a = [10.5, 20.0, 5.0, 8.0]
    b = [10.5, 15.0, 5.0, 12.0]
    output = compare_lengths(a, b)
    print(output)