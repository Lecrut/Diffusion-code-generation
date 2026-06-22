from functools import lru_cache

class FibonacciCalculator:
    @staticmethod
    @lru_cache(maxsize=None)
    def compute(n: int) -> int:
        if n < 0:
            raise ValueError("n must be non-negative")
        if n < 2:
            return n
        return FibonacciCalculator.compute(n - 1) + FibonacciCalculator.compute(n - 2)

if __name__ == '__main__':
    calculator = FibonacciCalculator()
    target_index = 30
    result = calculator.compute(target_index)
    print(result)