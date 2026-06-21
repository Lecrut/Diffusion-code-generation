class FibonacciGenerator:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1

    @staticmethod
    def _generate_fibonacci(n):
        fib_numbers = []
        for _ in range(n):
            fib_numbers.append(FibonacciGenerator._a)
            FibonacciGenerator._a, FibonacciGenerator._b = FibonacciGenerator._b, FibonacciGenerator._a + FibonacciGenerator._b
        return fib_numbers

    @property
    def result(self):
        return self._generate_fibonacci(self.n)

if __name__ == '__main__':
    generator = FibonacciGenerator(10)
    print(generator.result)