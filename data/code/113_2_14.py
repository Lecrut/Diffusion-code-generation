class PrecisionCalculator:
    def subtract(self, num1, num2):
        return num1 - num2

if __name__ == '__main__':
    calculator = PrecisionCalculator()
    result1 = calculator.subtract(3.141592653589793, 2.718281828459045)
    print(result1)