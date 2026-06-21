class SumCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_sum(self):
        return sum(self.numbers)

if __name__ == '__main__':
    calculator = SumCalculator([10, 25, 30, 45, 50])
    print(calculator.calculate_sum())