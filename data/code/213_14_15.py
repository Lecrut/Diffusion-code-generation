class FibonacciGenerator:
    def __init__(self, n):
        self.n = n
        self.fib_sequence = []

    def generate_fibonacci(self):
        a, b = 0, 1
        for _ in range(self.n):
            self.fib_sequence.append(a)
            a, b = b, a + b

if __name__ == '__main__':
    generator = FibonacciGenerator(10)
    generator.generate_fibonacci()
    print(generator.fib_sequence)