class SumCalculator:
    @staticmethod
    def calculate(a, b):
        return a + b

if __name__ == '__main__':
    result = SumCalculator.calculate(4, 6)
    print(result)