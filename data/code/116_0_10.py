class SumCalculator:
    NUM1 = 10
    NUM2 = 20
    NUM3 = 30

    @staticmethod
    def calculate_sum(a, b, c):
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum(SumCalculator.NUM1, SumCalculator.NUM2, SumCalculator.NUM3)
    print(result)