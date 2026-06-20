import numpy as np

def compare_lengths(array_a, array_b):
    a = np.asarray(array_a)
    b = np.asarray(array_b)
    diff = a - b
    return np.sign(diff)

if __name__ == '__main__':
    lengths_1 = np.array([10.5, 20.0, 15.3, 0.0, -5.2])
    lengths_2 = np.array([10.5, 19.5, 16.0, 5.0, -5.2])
    result = compare_lengths(lengths_1, lengths_2)
    print(result)