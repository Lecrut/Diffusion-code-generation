class FibonacciGenerator:
    def __init__(self):
        self.sequence = [0, 1]

    @staticmethod
    def calculate_next_fib(a, b):
        return a + b

    def generate_sequence(self, n):
        if n <= 2:
            return self.sequence[:n]
        
        for _ in range(2, n):
            next_val = self.calculate_next_fib(self.sequence[-1], self.sequence[-2])
            self.sequence.append(next_val)
        
        return self.sequence

if __name__ == '__main__':
    generator = FibonacciGenerator()
    fib_sequence = generator.generate_sequence(10)
    print(fib_sequence)