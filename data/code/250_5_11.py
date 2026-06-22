import numpy as np

AVERAGE_CALCULATION_THRESHOLD = 1000

class CustomAverageCalculator:
    def __init__(self):
        self.data = []
    
    def add_data(self, value):
        if len(self.data) == AVERAGE_CALCULATION_THRESHOLD:
            self.data.pop(0)
        self.data.append(value)
    
    def calculate_average(self):
        return np.mean(self.data)

if __name__ == '__main__':
    calculator = CustomAverageCalculator()
    for i in range(1500):
        calculator.add_data(i)
    print(calculator.calculate_average())