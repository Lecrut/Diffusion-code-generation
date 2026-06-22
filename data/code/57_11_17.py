from functools import lru_cache
import functools

class FibonacciCalculator:
    @staticmethod
    @functools.lru_cache(maxsize=None)
    def compute(n):
        if n < 0:
            raise ValueError("Index must be non-negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return FibonacciCalculator.compute(n - 1) + FibonacciCalculator.compute(n - 2)

if __name__ == '__main__':
    result = FibonacciCalculator.compute(30)
    print(result)