class SumCalculator:
    DEFAULT_A = 3.14
    DEFAULT_B = 2.72

    @staticmethod
    def sum_values(a, b):
        return a + b

    def __init__(self, a=DEFAULT_A, b=DEFAULT_B):
        self.a = a
        self.b = b

    def generate_sum(self):
        yield self.sum_values(self.a, self.b)

if __name__ == '__main__':
    calculator = SumCalculator(5.0, 10.0)
    result = next(calculator.generate_sum())
    print(result)