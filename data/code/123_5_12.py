import numpy as np

class CumulativeSumCalculator:
    def __init__(self, data):
        self.data = np.array(data)

    def calculate_cumulative_sum(self):
        return np.cumsum(self.data)

if __name__ == '__main__':
    calculator = CumulativeSumCalculator([1, 2, 3, 4, 5])
    cumulative_sum_result = calculator.calculate_cumulative_sum()
    print(cumulative_sum_result)