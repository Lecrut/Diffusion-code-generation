class HighPrecisionCalculator:
    def subtract(self, amount1, amount2):
        return amount1 - amount2

if __name__ == '__main__':
    calculator = HighPrecisionCalculator()
    result1 = calculator.subtract(3.141592653589793, 2.718281828459045)
    result2 = calculator.subtract(100.0, 45.0)
    print(result1)
    print(result2)