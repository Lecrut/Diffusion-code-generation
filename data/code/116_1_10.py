class SumCalculator:
    def calculate_sum(self, a: float, b: float, c: float) -> float:
        return a + b + c

if __name__ == '__main__':
    calculator = SumCalculator()
    result1 = calculator.calculate_sum(1.5, 2.5, 3.0)
    print(f"Result 1: {result1}")
    result2 = calculator.calculate_sum(4.0, 5.0, 6.0)
    print(f"Result 2: {result2}")