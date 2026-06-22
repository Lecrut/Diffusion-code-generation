class FibonacciGenerator:
    def __init__(self):
        self._cache = [0, 1]

    def _ensure_cache(self, n):
        while len(self._cache) < n:
            self._cache.append(self._cache[-1] + self._cache[-2])

    def get_sequence(self, count):
        self._ensure_cache(count)
        return self._cache[:count]

if __name__ == '__main__':
    generator = FibonacciGenerator()
    sequence = generator.get_sequence(150)
    print(sequence)