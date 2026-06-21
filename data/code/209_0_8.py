import statistics

class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_mean(self):
        return statistics.mean(self.numbers)

if __name__ == '__main__':
    calculator = AverageCalculator([10, 20, 30, 40, 50])
    average = calculator.calculate_mean()
    print(average)