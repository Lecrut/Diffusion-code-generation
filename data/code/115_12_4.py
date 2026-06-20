import numpy as np

def divide_array_by_scalar(numbers, divisor):
    return numbers / divisor if divisor != 0 else np.zeros_like(numbers)

if __name__ == '__main__':
    sample_numbers = np.array([10, 20, 30, 40, 50])
    scalar_divisor = 5
    result = divide_array_by_scalar(sample_numbers, scalar_divisor)
    print(result)