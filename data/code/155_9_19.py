import numpy as np

class SumCalculator:
    def __init__(self, numbers):
        self.numbers = np.array(numbers)

    def calculate_sum(self):
        return self.numbers.sum()

if __name__ == '__main__':
    calculator = SumCalculator([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    result = calculator.calculate_sum()
    print(f"Sum of numbers: {result}")