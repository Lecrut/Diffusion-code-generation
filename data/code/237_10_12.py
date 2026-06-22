class FibonacciGenerator:
    def __init__(self):
        self.a = 0
        self.b = 1
    
    def next(self):
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current

if __name__ == '__main__':
    fib_gen = FibonacciGenerator()
    sequence = [fib_gen.next() for _ in range(20)]
    print(sequence)