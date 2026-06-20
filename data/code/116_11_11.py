class SumCalculator:
    def __init__(self):
        self.numbers = [10, 25, 40]

    def calculate_sum(self):
        return sum(self.numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum()
    print(result)