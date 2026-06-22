class FibonacciSequence:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.index = 0
        self.cache = [0, 1]

    def generate(self, n):
        if n == 0:
            return []
        if n == 1:
            return [0]
        
        if self.index < n:
            start_index = self.index
            for i in range(start_index, n):
                next_val = self.a + self.b
                self.cache.append(next_val)
                self.a = self.b
                self.b = next_val
                self.index += 1
        return self.cache[:n]

if __name__ == '__main__':
    fib_gen = FibonacciSequence()
    result = fib_gen.generate(150)
    print(result)