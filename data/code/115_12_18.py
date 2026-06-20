import numpy as np
SCALAR_DIVISOR = 3

def divide_by_scalar(numbers):
    return numbers / SCALAR_DIVISOR
if __name__ == '__main__':
    sample_numbers = np.array([12, 45, 67, 89, 23])
    result = divide_by_scalar(sample_numbers)
    print(result)