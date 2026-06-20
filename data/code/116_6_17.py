class SumCalculator:
    @staticmethod
    def add_three_numbers(a, b, c):
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.add_three_numbers(5, 3, 8)
    print(result)