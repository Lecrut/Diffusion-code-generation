class PrecisionCalculator:
    def sum_with_precision(self, a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    calc = PrecisionCalculator()
    result1 = calc.sum_with_precision(0.1, 0.2)
    result2 = calc.sum_with_precision(3.141592653589793, 2.718281828459045)
    print(result1)
    print(result2)