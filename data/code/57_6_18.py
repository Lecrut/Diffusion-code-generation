class FibonacciSequence:
    def __init__(self):
        self._a = 0
        self._b = 1
        self._index = 0
        self._start_sequence = [0]

    def _extend(self, target_count):
        count = len(self._start_sequence)
        if target_count <= count:
            return
        last_val = self._start_sequence[-1]
        second_last = self._start_sequence[-2]
        for _ in range(target_count - count):
            new_val = last_val + second_last
            self._start_sequence.append(new_val)
            second_last = last_val
            last_val = new_val

    def get_first(self, n):
        self._extend(n)
        return self._start_sequence[:n]

if __name__ == '__main__':
    fib_class = FibonacciSequence()
    result = fib_class.get_first(150)
    print(result[0])
    print(result[-1])
    print(result[10])
    print(result[50])