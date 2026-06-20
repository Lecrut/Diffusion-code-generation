class PrecisionCalculator:
    PRECISION = 1e-10

    @staticmethod
    def subtract(amount1, amount2):
        return amount1 - amount2 if abs(amount1 - amount2) > PrecisionCalculator.PRECISION else 0.0

if __name__ == '__main__':
    calculator = PrecisionCalculator()
    result = calculator.subtract(3.141592653589793, 2.718281828459045)
    print(result)