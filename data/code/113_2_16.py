class PrecisionCalculator:
    def subtract(self, amount1, amount2):
        return amount1 - amount2

if __name__ == '__main__':
    calculator = PrecisionCalculator()
    result1 = calculator.subtract(100.0, 45.0)
    result2 = calculator.subtract(3.141592653589793, 2.718281828459045)
    result3 = calculator.subtract(23.4567890123456789, 12.3456789012345678)
    print(result1)
    print(result2)
    print(result3)