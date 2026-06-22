import numpy as np

class MeanCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def compute_mean(self):
        if isinstance(self.numbers, np.ndarray):
            return np.mean(self.numbers)
        else:
            return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5]
    calculator = MeanCalculator(sample_numbers)
    print(calculator.compute_mean())