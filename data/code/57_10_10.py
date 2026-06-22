class FibonacciGenerator:
    LIMIT = 10

    @staticmethod
    def _get_terms():
        yield 0
        yield 1
        a, b = 0, 1
        for _ in range(FibonacciGenerator.LIMIT - 2):
            a, b = b, a + b
            yield b

    def get_fibonacci_sequence(self):
        return list(FibonacciGenerator._get_terms())

if __name__ == '__main__':
    gen = FibonacciGenerator()
    result = gen.get_fibonacci_sequence()
    print(result)