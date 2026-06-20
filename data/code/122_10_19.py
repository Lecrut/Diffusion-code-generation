import statistics

class MeanCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_mean(self):
        return statistics.mean(self.numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 6.7, 5.0]
    calculator = MeanCalculator(sample_numbers)
    mean_value = calculator.calculate_mean()
    print(mean_value)