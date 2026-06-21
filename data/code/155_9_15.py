import numpy as np

class SumCalculator:
    def __init__(self):
        self.numbers = np.random.randint(0, 100, size=10)

    def calculate_sum(self):
        return self.numbers.sum()

if __name__ == '__main__':
    calculator = SumCalculator()
    print(f"Random Numbers: {calculator.numbers}")
    print(f"Sum of Numbers: {calculator.calculate_sum()}")