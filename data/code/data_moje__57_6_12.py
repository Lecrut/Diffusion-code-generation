class FibonacciGenerator:
    def __init__(self, count):
        self.count = count
        self._sequence = []
        self._a = 0
        self._b = 1
        self._generate()

    def _generate(self):
        for _ in range(self.count):
            self._sequence.append(self._a)
            next_val = self._a + self._b
            self._a = self._b
            self._b = next_val

    def get_sequence(self):
        return self._sequence

if __name__ == '__main__':
    gen = FibonacciGenerator(150)
    seq = gen.get_sequence()
    print(seq)