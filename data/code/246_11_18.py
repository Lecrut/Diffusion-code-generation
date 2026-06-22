class PrecisionCalculator:
    def sum_two_numbers(self, a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    calculator = PrecisionCalculator()
    result1 = calculator.sum_two_numbers(0.1, 0.2)
    result2 = calculator.sum_two_numbers(3.141592653589793, 2.718281828459045)
    result3 = calculator.sum_two_numbers(123.4567890123456789, 987.6543210987654321)
    print(result1)
    print(result2)
    print(result3)