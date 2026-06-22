class FibonacciGenerator:
    def __init__(self):
        self._cache = []

    def generate(self, count):
        if len(self._cache) >= count:
            return self._cache[:count]
        if not self._cache:
            self._cache = [0, 1]
            if count <= 2:
                return self._cache[:count]
        current_len = len(self._cache)
        while len(self._cache) < count:
            next_val = self._cache[-1] + self._cache[-2]
            self._cache.append(next_val)
        return self._cache[:count]

if __name__ == '__main__':
    gen = FibonacciGenerator()
    result = gen.generate(150)
    print(result)