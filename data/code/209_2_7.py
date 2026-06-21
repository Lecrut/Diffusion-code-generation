import numpy as np

class AverageCalculator:
    def __init__(self, values):
        self.values = values
    
    def calculate_average(self):
        return np.mean(self.values)

if __name__ == '__main__':
    calculator = AverageCalculator([100, 200, 300])
    average = calculator.calculate_average()
    print(average)