import numpy as np

class ArrayDivider:
    SCALAR_DIVISOR = 5

    @staticmethod
    def divide_by_scalar(numbers):
        return numbers / ArrayDivider.SCALAR_DIVISOR

if __name__ == '__main__':
    sample_numbers = np.array([10, 20, 30, 40, 50])
    result = ArrayDivider.divide_by_scalar(sample_numbers)
    print(result)