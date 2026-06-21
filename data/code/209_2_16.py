import numpy as np

class AverageCalculator:
    def __init__(self, values):
        self.values = values
    
    def validate_values(self):
        if not all(isinstance(x, (int, float)) for x in self.values):
            raise ValueError("All elements in the input list must be integers or floats.")
    
    def calculate_average(self):
        return np.mean(self.values)

if __name__ == '__main__':
    calculator = AverageCalculator([100, 200, 300])
    calculator.validate_values()
    average = calculator.calculate_average()
    print(average)