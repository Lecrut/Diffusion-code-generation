import numpy as np

def divide_arrays(a, b):
    result = np.where(b != 0, a / b, 0)
    return result

if __name__ == '__main__':
    sample_a = np.array([1, 2, 3, 4])
    sample_b = np.array([2, 0, 4, 0])
    print(divide_arrays(sample_a, sample_b))