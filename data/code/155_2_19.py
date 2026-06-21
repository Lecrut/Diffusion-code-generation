class FloatSumCalculator:
    def __init__(self):
        self.total = 0.0

    def add_number(self, number):
        self.total += number

    def get_sum(self):
        return self.total

if __name__ == '__main__':
    calculator = FloatSumCalculator()
    calculator.add_number(1.5)
    calculator.add_number(2.75)
    calculator.add_number(3.0)
    calculator.add_number(-4.2)
    calculator.add_number(0.1)
    result = calculator.get_sum()
    print(result)