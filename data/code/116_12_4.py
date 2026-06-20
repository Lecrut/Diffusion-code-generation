class SumCalculator:
    def sum(self, a: float, b: float, c: float) -> float:
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    num1 = 10.5
    num2 = 20.3
    num3 = 30.7
    result = calculator.sum(num1, num2, num3)
    print(result)