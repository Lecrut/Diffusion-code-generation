class SumCalculator:
    def __init__(self, a, b, c):
        self.numbers = (a, b, c)

    def calculate_sum(self):
        return sum(self.numbers)

if __name__ == '__main__':
    calculator = SumCalculator(10, 20, 30)
    result = calculator.calculate_sum()
    print(result)