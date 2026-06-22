import numpy as np

class AverageCalculator:
    def __init__(self, data):
        self.data = np.array(data)

    def calculate_average(self):
        return np.mean(self.data)

if __name__ == '__main__':
    calculator = AverageCalculator([10, 20, 30, 40, 50])
    print(calculator.calculate_average())