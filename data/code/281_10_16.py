class SumCalculator:
    def __init__(self):
        self.values = [5, 7, 9]

    def calculate_sum(self):
        return sum(self.values)

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum()
    print(result)