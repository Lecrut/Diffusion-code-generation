class FloatSumCalculator:

    def sum_floats(self, a: float, b: float, c: float) -> float:
        return a + b + c
if __name__ == '__main__':
    calculator = FloatSumCalculator()
    result1 = calculator.sum_floats(1.0, 2.0, 3.0)
    result2 = calculator.sum_floats(-1.1, 2.2, -3.3)
    print(result1)
    print(result2)