class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

if __name__ == '__main__':
    calculator = AverageCalculator([1.5, 2.5, 3.5])
    print(calculator.calculate())