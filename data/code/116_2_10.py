class SumCalculator:
    @staticmethod
    def sum_three(a, b, c):
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.sum_three(10, 20, 30)
    print(result)