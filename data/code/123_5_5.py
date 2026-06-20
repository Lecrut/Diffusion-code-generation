import numpy as np

class CumulativeSumCalculator:
    def __init__(self, data):
        self.data = np.array(data)

    def compute_cumulative_sum(self):
        return np.cumsum(self.data)

if __name__ == '__main__':
    calculator = CumulativeSumCalculator([1, 2, 3, 4, 5])
    result = calculator.compute_cumulative_sum()
    print(result)