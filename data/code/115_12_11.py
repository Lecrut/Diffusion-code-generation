import numpy as np

def divide_by_scalar(numbers, divisor):
    return numbers / divisor

if __name__ == '__main__':
    sample_numbers = np.array([120, 345, 678, 901, 234])
    scalar_divisor = 10
    result = divide_by_scalar(sample_numbers, scalar_divisor)
    print(result)