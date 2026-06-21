import numpy as np

class AverageCalculator:
    def __init__(self, data):
        self.data = np.array(data)

    def compute_average(self):
        return np.mean(self.data)

if __name__ == '__main__':
    calculator = AverageCalculator([100, 200, 300])
    average = calculator.compute_average()
    print(average)