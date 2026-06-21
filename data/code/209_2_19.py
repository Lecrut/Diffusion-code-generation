import numpy as np

class AverageCalculator:
    def __init__(self, values):
        self.values = values
    
    def calculate_average(self):
        if not all(isinstance(x, (int, float)) for x in self.values):
            raise ValueError("All elements in the input list must be integers or floats.")
        return np.mean(self.values)

if __name__ == '__main__':
    calculator = AverageCalculator([100, 200, 300])
    average = calculator.calculate_average()
    print(average)