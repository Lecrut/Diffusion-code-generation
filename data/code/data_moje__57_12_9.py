class FibonacciGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.sequence = [0, 1]
        self._build_sequence()

    def _build_sequence(self):
        a, b = 0, 1
        while len(self.sequence) < self.limit:
            a, b = b, a + b
            self.sequence.append(a)
        self.sequence = self.sequence[:self.limit]

    def get_sequence(self):
        return self.sequence

if __name__ == '__main__':
    generator = FibonacciGenerator(20)
    print(generator.get_sequence())