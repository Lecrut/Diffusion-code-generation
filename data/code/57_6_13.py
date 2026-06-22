class FibonacciGenerator:
    def __init__(self):
        self._cache = [0, 1]

    def generate_sequence(self, count):
        while len(self._cache) < count:
            next_val = self._cache[-1] + self._cache[-2]
            self._cache.append(next_val)
        return self._cache[:count]

if __name__ == '__main__':
    fib_gen = FibonacciGenerator()
    result = fib_gen.generate_sequence(150)
    print(result)