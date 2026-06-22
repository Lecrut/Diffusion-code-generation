class FibonacciGenerator:
    def __init__(self):
        self._cache = [0, 1]

    def generate(self, n):
        if n <= 2:
            return self._cache[:n]
        cache = self._cache
        for i in range(2, n):
            cache.append(cache[i - 1] + cache[i - 2])
        return cache

if __name__ == '__main__':
    gen = FibonacciGenerator()
    print(gen.generate(15))