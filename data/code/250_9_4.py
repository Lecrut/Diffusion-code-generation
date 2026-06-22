import math

class MeanCalculator:
    def __init__(self, numbers: list):
        self.numbers = numbers
    
    def calculate_mean(self) -> float:
        if len(self.numbers) == 0:
            return 0.0
        total_sum = math.fsum(self.numbers)
        count = len(self.numbers)
        return total_sum / count

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    calculator = MeanCalculator(sample_numbers)
    mean_value = calculator.calculate_mean()
    print(mean_value)