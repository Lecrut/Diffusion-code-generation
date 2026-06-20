import numpy as np

def divide_numbers(numbers, divisor):
    return numbers / divisor

if __name__ == '__main__':
    sample_numbers = np.array([10, 20, 30, 40, 50])
    divisor = 5
    result = divide_numbers(sample_numbers, divisor)
    print(result)