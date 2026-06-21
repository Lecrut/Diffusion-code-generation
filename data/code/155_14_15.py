class FloatSumCalculator:
    def __init__(self):
        self.total = 0.0

    def add(self, value):
        self.total += value

    def get_total(self):
        return self.total

if __name__ == '__main__':
    calculator = FloatSumCalculator()
    values = [1.5, 2.5, 3.5]
    for value in values:
        calculator.add(value)
    result = calculator.get_total()
    print(result)