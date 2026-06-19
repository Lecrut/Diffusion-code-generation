class SumCalculator:
    DEFAULT_VALUE_A = 10
    DEFAULT_VALUE_B = 20

    @staticmethod
    def sum_values(a, b):
        return a + b

    @classmethod
    def generate_sum(cls, a=None, b=None):
        if a is None:
            a = cls.DEFAULT_VALUE_A
        if b is None:
            b = cls.DEFAULT_VALUE_B
        yield cls.sum_values(a, b)

if __name__ == '__main__':
    calculator = SumCalculator()
    result = next(calculator.generate_sum(3.14159, 2.71828))
    print(result)