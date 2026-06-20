class SumCalculator:
    @staticmethod
    def calculate_sum(a: float, b: float, c: float) -> float:
        return a + b + c

if __name__ == '__main__':
    result1 = SumCalculator.calculate_sum(1.5, 2.5, 3.0)
    print(f"Result 1: {result1}")