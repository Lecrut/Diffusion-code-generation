class NumberRangeCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_range(self):
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    calculator = NumberRangeCalculator([3, 5, 1, 8, 2])
    print(calculator.calculate_range())