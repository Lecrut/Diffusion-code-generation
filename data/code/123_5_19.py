import numpy as np

class CumulativeSumCalculator:
    def __init__(self, data):
        self.data = np.array(data)
    
    def calculate_cumsum(self):
        return np.cumsum(self.data)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    calculator = CumulativeSumCalculator(sample_data)
    cumulative_sum_result = calculator.calculate_cumsum()
    print(cumulative_sum_result)