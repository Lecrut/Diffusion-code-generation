import numpy as np

class VectorizedDivider:
    DIVISOR = 5

    @staticmethod
    def divide_by_scalar(numbers):
        return numbers / VectorizedDivider.DIVISOR

if __name__ == '__main__':
    sample_numbers = np.array([10, 20, 30, 40, 50])
    result = VectorizedDivider.divide_by_scalar(sample_numbers)
    print(result)