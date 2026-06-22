class FibonacciGenerator:
    def __init__(self):
        self._cache = [0, 1]

    def generate_sequence(self, count):
        while len(self._cache) < count:
            self._cache.append(self._cache[-1] + self._cache[-2])
        return self._cache[:count]

if __name__ == '__main__':
    generator = FibonacciGenerator()
    result = generator.generate_sequence(150)
    print(result)