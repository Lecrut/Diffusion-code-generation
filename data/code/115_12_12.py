import numpy as np

def divide_by_scalar(numbers, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return numbers / divisor

if __name__ == '__main__':
    sample_numbers = np.array([10, 20, 30, 40, 50])
    scalar_divisor = 5
    result = divide_by_scalar(sample_numbers, scalar_divisor)
    print(result)