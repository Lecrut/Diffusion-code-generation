class FibonacciGenerator:
    def __init__(self, count):
        self.count = count
        self.sequence = self._compute()

    def _compute(self):
        if self.count <= 0:
            return []
        if self.count == 1:
            return [0]
        result = [0, 1]
        a, b = 0, 1
        for _ in range(2, self.count):
            a, b = b, a + b
            result.append(b)
        return result

    def get_list(self):
        return self.sequence

    def get_sum(self):
        return sum(self.sequence)

    def get_last(self):
        if not self.sequence:
            return None
        return self.sequence[-1]

if __name__ == '__main__':
    gen = FibonacciGenerator(20)
    print(gen.get_list())
    print(gen.get_sum())
    print(gen.get_last())