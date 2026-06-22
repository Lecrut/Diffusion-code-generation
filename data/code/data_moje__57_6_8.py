class FibonacciSequence:
    def __init__(self):
        self._sequence = [0, 1]
        self._generated = 2
        for _ in range(148):
            next_val = self._sequence[-1] + self._sequence[-2]
            self._sequence.append(next_val)
            self._generated += 1

    def get_sequence(self, count):
        if count <= 0:
            return []
        if count > len(self._sequence):
            while len(self._sequence) < count:
                next_val = self._sequence[-1] + self._sequence[-2]
                self._sequence.append(next_val)
        return self._sequence[:count]

if __name__ == '__main__':
    fib = FibonacciSequence()
    first_150 = fib.get_sequence(150)
    print(first_150[-1])
    print(first_150[:10])