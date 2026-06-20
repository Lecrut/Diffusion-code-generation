class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    calculator1 = AverageCalculator([1, 2, 3, 4, 5])
    print(f"Average of [1, 2, 3, 4, 5]: {calculator1.calculate()}")

    calculator2 = AverageCalculator([])
    print(f"Average of []: {calculator2.calculate()}")

    calculator3 = AverageCalculator([10, 20, 30])
    print(f"Average of [10, 20, 30]: {calculator3.calculate()}")

    calculator4 = AverageCalculator([-1, 5, 10])
    print(f"Average of [-1, 5, 10]: {calculator4.calculate()}")