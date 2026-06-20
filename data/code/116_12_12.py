class FloatSumCalculator:
    def sum(self, a: float, b: float, c: float) -> float:
        return a + b + c

if __name__ == '__main__':
    calculator = FloatSumCalculator()
    num1 = 1.123456789
    num2 = 2.234567890
    num3 = 3.345678901
    result = calculator.sum(num1, num2, num3)
    print(result)