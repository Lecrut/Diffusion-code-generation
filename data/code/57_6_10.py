class FibonacciGenerator:
    def __init__(self):
        self._a = 0
        self._b = 1
        self._count = 0

    def _reset(self):
        self._a = 0
        self._b = 1
        self._count = 0

    def generate_first_n(self, n):
        self._reset()
        sequence = []
        for _ in range(n):
            sequence.append(self._a)
            self._a, self._b = self._b, self._a + self._b
        return sequence

if __name__ == '__main__':
    generator = FibonacciGenerator()
    result = generator.generate_first_n(150)
    print(result)