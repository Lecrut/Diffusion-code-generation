class FactorialEngine:
    def __init__(self):
        self._limit = 1000

    def get_factorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Input must be a non-negative integer")
        if n > self._limit:
            raise ValueError("Input exceeds supported limit")
        accumulator = 1
        for current in range(2, n + 1):
            accumulator *= current
        return accumulator

    def set_limit(self, new_limit):
        if new_limit < 0:
            raise ValueError("Limit cannot be negative")
        self._limit = new_limit

if __name__ == '__main__':
    engine = FactorialEngine()
    test_cases = [0, 1, 6, 12]
    results = []
    for value in test_cases:
        results.append(engine.get_factorial(value))
    print(results)