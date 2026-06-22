class FibonacciGenerator:
    def __init__(self, n):
        self.n = n
        self.cache = [0, 1]

    def generate(self):
        results = []
        for i in range(self.n):
            if i < len(self.cache):
                results.append(self.cache[i])
            else:
                next_val = self.cache[-1] + self.cache[-2]
                self.cache.append(next_val)
                results.append(next_val)
        return results

if __name__ == '__main__':
    generator = FibonacciGenerator(150)
    print(generator.generate())