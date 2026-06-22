import numpy as np

class CustomAverageCalculator:
    def __init__(self):
        self.data = []
    
    def add_value(self, value):
        self.data.append(value)
    
    def compute_average(self):
        if not self.data:
            return 0.0
        return np.mean(np.array(self.data))

if __name__ == '__main__':
    calculator = CustomAverageCalculator()
    calculator.add_value(3)
    calculator.add_value(6)
    calculator.add_value(9)
    print(calculator.compute_average())