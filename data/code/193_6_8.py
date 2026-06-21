class NumericSumCalculator:
    def __init__(self):
        self.total = 0

    def add_number(self, number):
        if isinstance(number, int):
            self.total += number
        elif isinstance(number, float):
            self.total += number
        return self.total

if __name__ == '__main__':
    calculator = NumericSumCalculator()
    sample_values = [10, 2.5, -3, 4.75]
    for value in sample_values:
        print(calculator.add_number(value))