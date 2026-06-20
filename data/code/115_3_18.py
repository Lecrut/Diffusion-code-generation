class DivisionCalculator:
    @staticmethod
    def divide(numerator, denominator):
        return numerator / denominator

if __name__ == '__main__':
    calculator = DivisionCalculator()
    result = calculator.divide(10, 3)
    print(f"Result of division: {result}")