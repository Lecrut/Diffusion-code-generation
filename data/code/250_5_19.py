import numpy as np

class AverageCalculator:
    def __init__(self):
        self.data = []
    
    def add_data(self, value):
        self.data.append(value)
    
    def calculate_average(self):
        if not self.data:
            return 0.0
        return np.mean(np.array(self.data))

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add_data(5)
    calculator.add_data(10)
    calculator.add_data(15)
    print(calculator.calculate_average())