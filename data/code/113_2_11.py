class PrecisionCalculator:
    def subtract(self, amount1, amount2):
        return amount1 - amount2

if __name__ == '__main__':
    calculator = PrecisionCalculator()
    result1 = calculator.subtract(100.5, 45.2)
    result2 = calculator.subtract(3.141592653589793, 2.718281828459045)
    print(result1)
    print(result2)