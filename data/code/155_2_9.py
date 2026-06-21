class FloatSumCalculator:
    def __init__(self):
        self.total = 0.0

    def add_number(self, number):
        self.total += number

    def get_sum(self):
        return self.total

if __name__ == '__main__':
    calculator = FloatSumCalculator()
    sample_values = [1.5, 2.75, 3.0, -4.2, 0.1]
    for value in sample_values:
        calculator.add_number(value)
    result = calculator.get_sum()
    print(result)