import numpy as np

class AverageCalculator:
    def __init__(self):
        self.data = []
    
    def add_data(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Data must be a number")
        self.data.append(value)
    
    def calculate_average(self):
        if not self.data:
            return 0.0
        return np.mean(self.data)

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add_data(10)
    calculator.add_data(20)
    calculator.add_data(30)
    print(calculator.calculate_average())