class SumCalculator:
    @staticmethod
    def sum_three_numbers(a, b, c):
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.sum_three_numbers(3, 5, 7)
    print(result)