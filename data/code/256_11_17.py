class RangeCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_range(self):
        if not self.numbers:
            return 0
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    calculator = RangeCalculator([10, 5, 20, 15, 8])
    print(calculator.calculate_range())

    calculator = RangeCalculator([-1, -3, -5, -7, -9])
    print(calculator.calculate_range())

    calculator = RangeCalculator([1.5, 2.5, 3.5, 4.5, 5.5])
    print(calculator.calculate_range())