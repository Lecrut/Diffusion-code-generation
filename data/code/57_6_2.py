class FibonacciGenerator:
    def __init__(self):
        self.cache = [0, 1]

    def generate_first_n(self, n):
        if n <= 0:
            return []
        if n == 1:
            return [0]
        while len(self.cache) < n:
            next_val = self.cache[-1] + self.cache[-2]
            self.cache.append(next_val)
        return self.cache[:n]

if __name__ == '__main__':
    generator = FibonacciGenerator()
    result = generator.generate_first_n(150)
    print(result)