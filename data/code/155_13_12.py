class SumCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_sum(self):
        return sum(self.numbers)

if __name__ == '__main__':
    calculator = SumCalculator([1, 2, 3, 4, 5])
    total = calculator.calculate_sum()
    print("Total sum:", total)