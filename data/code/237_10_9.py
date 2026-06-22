class FibonacciGenerator:
    def __init__(self):
        self.sequence = [0, 1]

    @staticmethod
    def generate_next_term(a, b):
        return a + b

    def extend_sequence(self):
        if len(self.sequence) < 2:
            return
        last_two = self.sequence[-2:]
        next_term = self.generate_next_term(*last_two)
        self.sequence.append(next_term)

    def get_sequence(self, n):
        while len(self.sequence) < n:
            self.extend_sequence()
        return self.sequence[:n]

if __name__ == '__main__':
    fib_gen = FibonacciGenerator()
    print(fib_gen.get_sequence(20))