import numpy as np

class AverageCalculator:
    def __init__(self, data):
        self.data = np.array(data)
    
    def calculate_average(self):
        return np.mean(self.data)

if __name__ == '__main__':
    calculator = AverageCalculator([1.0, 2.0, 3.0, 4.0, 5.0])
    print("Average:", calculator.calculate_average())