class RangeCalculator:

    def __init__(self, numbers):
        self.numbers = sorted(set(numbers))

    def calculate_range(self):
        if not self.numbers:
            return None
        return (self.numbers[0], self.numbers[-1])
if __name__ == '__main__':
    calculator1 = RangeCalculator([10, 5, 22, 8, 15])
    print(calculator1.calculate_range())
    calculator2 = RangeCalculator([15, 3, 88, 42, 9])
    print(calculator2.calculate_range())