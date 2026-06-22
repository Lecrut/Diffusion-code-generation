class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate(self):
        if not self.numbers:
            return 0
        total = sum(self.numbers)
        count = len(self.numbers)
        average = total / count
        return average

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    calculator = AverageCalculator(sample_values)
    avg = calculator.calculate()
    print(avg)