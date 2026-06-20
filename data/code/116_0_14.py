class SumCalculator:
    def __init__(self):
        self.numbers = [10, 20, 30]

    def calculate_sum(self):
        return sum(self.numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum()
    print(result)