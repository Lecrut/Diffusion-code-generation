class SumCalculator:
    def calculate_sum(self, num1, num2, num3):
        return num1 + num2 + num3

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum(10, 20, 30)
    print(result)