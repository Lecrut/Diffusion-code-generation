import numpy as np

class AverageCalculator:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def calculate_average(self):
        if not self.data:
            return 0.0
        return np.mean(self.data)

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add(10)
    calculator.add(20)
    calculator.add(30)
    print(calculator.calculate_average())