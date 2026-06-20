import numpy as np

class CumulativeSumCalculator:
    def __init__(self, data):
        self.data = data

    def compute_cumulative_sum(self):
        return np.cumsum(self.data)

if __name__ == '__main__':
    sample_data = np.array([1, 2, 3, 4, 5])
    calculator = CumulativeSumCalculator(sample_data)
    cumulative_sum_result = calculator.compute_cumulative_sum()
    print(cumulative_sum_result)