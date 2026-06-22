class FibonacciGenerator:
    def __init__(self):
        self._sequence = [0, 1]
        self._index = 2

    def _ensure_up_to(self, n):
        while len(self._sequence) < n:
            next_val = self._sequence[-1] + self._sequence[-2]
            self._sequence.append(next_val)
            self._index = len(self._sequence)

    def get_sequence(self, count):
        self._ensure_up_to(count)
        return self._sequence[:count]

if __name__ == '__main__':
    fib_gen = FibonacciGenerator()
    first_150 = fib_gen.get_sequence(150)
    print(first_150)