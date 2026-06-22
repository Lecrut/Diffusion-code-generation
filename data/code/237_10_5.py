class FibonacciGenerator:
    def __init__(self):
        self.a, self.b = 0, 1

    def next_term(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

if __name__ == '__main__':
    fib_gen = FibonacciGenerator()
    sequence = [fib_gen.next_term() for _ in range(20)]
    print(sequence)