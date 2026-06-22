class SumCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_sum(self):
        return self.a + self.b

if __name__ == '__main__':
    calculator = SumCalculator(5, 10)
    result = calculator.calculate_sum()
    print(result)