class FibonacciGenerator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next_value(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def generate_sequence(self, n):
        if n <= 0:
            return []
        result = []
        for _ in range(n):
            result.append(self.next_value())
        return result

if __name__ == '__main__':
    fg = FibonacciGenerator()
    first_150 = fg.generate_sequence(150)
    print(first_150[:10])
    print(first_150[149])