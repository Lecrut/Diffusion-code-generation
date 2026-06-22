import numpy as np

class MeanCalculator:
    @staticmethod
    def compute_mean(numbers):
        if isinstance(numbers, np.ndarray) and numbers.dtype == np.float64:
            return np.mean(numbers)
        else:
            return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    calculator = MeanCalculator()
    print(calculator.compute_mean(sample_numbers))