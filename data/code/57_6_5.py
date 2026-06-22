class FibonacciGenerator:
    def __init__(self):
        self.cache = []

    def generate(self, n=150):
        if len(self.cache) >= n:
            return self.cache[:n]
        a, b = 0, 1
        for _ in range(n - len(self.cache)):
            self.cache.append(a)
            a, b = b, a + b
        return self.cache[:n]

if __name__ == '__main__':
    gen = FibonacciGenerator()
    result = gen.generate(150)
    print(result)