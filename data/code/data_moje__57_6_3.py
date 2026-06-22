class FibonacciGenerator:
    def __init__(self):
        self._cache = [0, 1]

    def generate(self, n):
        while len(self._cache) < n:
            next_value = self._cache[-1] + self._cache[-2]
            self._cache.append(next_value)
        return self._cache[:n]

if __name__ == '__main__':
    generator = FibonacciGenerator()
    result = generator.generate(150)
    print(result)