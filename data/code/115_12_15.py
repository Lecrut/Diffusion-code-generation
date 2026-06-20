import numpy as np

def divide_by_scalar(numbers, divisor):
    return numbers / divisor

if __name__ == '__main__':
    sample_numbers = np.array([100, 200, 300, 400, 500])
    scalar_divisor = 10
    result = divide_by_scalar(sample_numbers, scalar_divisor)
    print(result)