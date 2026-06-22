import numpy as np

class VectorizedAverageCalculator:
    def __init__(self):
        self.data = np.array([])
    
    def add_data(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a number.")
        self.data = np.append(self.data, value)
    
    def calculate_average(self):
        return np.mean(self.data) if len(self.data) > 0 else 0.0

if __name__ == '__main__':
    calculator = VectorizedAverageCalculator()
    calculator.add_data(10)
    calculator.add_data(20)
    calculator.add_data(30)
    print(calculator.calculate_average())