import numpy as np

def compare_signs(lengths_a, lengths_b):
    lengths_a = np.asarray(lengths_a)
    lengths_b = np.asarray(lengths_b)
    diff = lengths_a - lengths_b
    return np.sign(diff)

if __name__ == '__main__':
    array_a = np.array([10.0, 5.5, 0.0, 15.2, -3.0])
    array_b = np.array([8.0, 5.5, 2.0, 10.0, 4.0])
    result = compare_signs(array_a, array_b)
    print(result)