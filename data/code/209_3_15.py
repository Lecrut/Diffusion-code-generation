class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate(self):
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    calculator = AverageCalculator([5, 10, 15, 20, 25])
    average = calculator.calculate()
    print(average)