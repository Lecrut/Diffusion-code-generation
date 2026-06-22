class SumCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

if __name__ == '__main__':
    calculator = SumCalculator(3.14159, 2.71828)
    print(calculator.sum())