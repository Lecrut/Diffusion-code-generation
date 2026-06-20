import numpy as np

def divide_array_by_scalar(arr, scalar):
    return arr / scalar

if __name__ == '__main__':
    sample_numbers = np.array([12, 45, 67, 89, 23])
    divisor = 3
    result = divide_array_by_scalar(sample_numbers, divisor)
    print(result)