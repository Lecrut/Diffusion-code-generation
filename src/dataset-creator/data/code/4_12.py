class SumCalculator:
    def calculate_sum(self, a, b, c):
        return a + b + c
if __name__ == '__main__':
    calculator = SumCalculator()
    num1 = 10
    num2 = 20
    num3 = 30
    result = calculator.calculate_sum(num1, num2, num3)
    print(result)