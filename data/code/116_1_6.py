class SumCalculator:
    def sum_three_floats(self, a: float, b: float, c: float) -> float:
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.sum_three_floats(1.5, 2.5, 3.0)
    print(f"Result 1: {result1}")
    result2 = calculator.sum_three_floats(4.5, 5.5, 6.0)
    print(f"Result 2: {result2}")