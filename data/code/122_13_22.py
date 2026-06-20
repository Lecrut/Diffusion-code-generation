class StatisticsCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_mean(self):
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    calculator = StatisticsCalculator([3.5, 2.1, 4.8, 6.7])
    print(calculator.calculate_mean())