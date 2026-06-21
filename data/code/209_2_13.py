import numpy as np

class AverageCalculator:
    @staticmethod
    def calculate_average(values):
        if not all(isinstance(x, (int, float)) for x in values):
            raise ValueError("All elements in the input list must be integers or floats.")
        return np.mean(values)

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    try:
        calculator = AverageCalculator()
        average = calculator.calculate_average(sample_values)
        print(average)
    except ValueError as e:
        print(e)