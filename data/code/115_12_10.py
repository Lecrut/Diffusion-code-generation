import numpy as np
SCALAR_DIVISOR = 2

def divide_by_scalar(numbers):
    return numbers / SCALAR_DIVISOR
if __name__ == '__main__':
    sample_numbers = np.array([10, 20, 30, 40, 50])
    result = divide_by_scalar(sample_numbers)
    print(result)