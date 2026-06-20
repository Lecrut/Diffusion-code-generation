class SumCalculator:
    CONSTANT_NUM1 = 10
    CONSTANT_NUM2 = 20
    CONSTANT_NUM3 = 30

    @staticmethod
    def calculate_sum(a, b, c):
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum(SumCalculator.CONSTANT_NUM1, SumCalculator.CONSTANT_NUM2, SumCalculator.CONSTANT_NUM3)
    print(result)