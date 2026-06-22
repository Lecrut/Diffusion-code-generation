class SumCalculator:
    @staticmethod
    def calculate_sum(a, b, c):
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum(5, 7, 9)
    print(result)