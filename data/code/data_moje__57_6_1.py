class FibonacciGenerator:
    def __init__(self):
        self._cache = [0, 1]

    def generate(self, n):
        while len(self._cache) < n:
            self._cache.append(self._cache[-1] + self._cache[-2])
        return self._cache[:n]

if __name__ == '__main__':
    gen = FibonacciGenerator()
    result = gen.generate(150)
    print(result)