class SumCalculator:
    def add_numbers(self, a, b):
        return a + b

if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.add_numbers(5, 3)
    result2 = calculator.add_numbers(7, 9)
    print(result1)
    print(result2)