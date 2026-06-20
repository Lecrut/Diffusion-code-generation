import numpy as np

def divide_by_scalar(numbers, divisor):
    return numbers / divisor

if __name__ == '__main__':
    sample_numbers = np.array([15, 25, 35, 45, 55])
    scalar_divisor = 5
    result = divide_by_scalar(sample_numbers, scalar_divisor)
    print(result)