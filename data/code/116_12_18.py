class FloatSumCalculator:
    def sum_floats(self, a: float, b: float, c: float) -> float:
        return a + b + c

if __name__ == '__main__':
    calculator = FloatSumCalculator()
    sample_a = 1.23456789
    sample_b = 2.34567890
    sample_c = 3.45678901
    result = calculator.sum_floats(sample_a, sample_b, sample_c)
    print(result)