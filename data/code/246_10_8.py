class SumCalculator:
    @staticmethod
    def add_numbers(a, b):
        return a + b

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.add_numbers(15, 27)
    print(result)