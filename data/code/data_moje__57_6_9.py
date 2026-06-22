class FibonacciGenerator:
    def __init__(self):
        self._cache = [0, 1]

    def _ensure_cache(self, n):
        if n < 2:
            return
        current_len = len(self._cache)
        if n >= current_len:
            a, b = self._cache[-2], self._cache[-1]
            for _ in range(current_len, n + 1):
                a, b = b, a + b
                self._cache.append(b)

    def get_sequence(self, count):
        self._ensure_cache(count - 1)
        return self._cache[:count]

if __name__ == '__main__':
    gen = FibonacciGenerator()
    sequence = gen.get_sequence(150)
    for num in sequence:
        print(num)