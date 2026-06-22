class FibonacciGenerator:
    def __init__(self):
        self._cache = [0, 1]

    def _extend_cache(self, n):
        while len(self._cache) <= n:
            self._cache.append(self._cache[-1] + self._cache[-2])

    def get_sequence(self, count):
        if count <= 0:
            return []
        self._extend_cache(count - 1)
        return self._cache[:count]

if __name__ == '__main__':
    generator = FibonacciGenerator()
    fib_150 = generator.get_sequence(150)
    print(fib_150)