class SumCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

if __name__ == '__main__':
    calculator = SumCalculator(20, 35)
    print(calculator.get_sum())
    print(calculator.get_sum() * 2)