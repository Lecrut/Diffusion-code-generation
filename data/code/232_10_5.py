class FibonacciGenerator:
    def __init__(self):
        self.sequence = [1, 2]

    def next_number(self):
        if len(self.sequence) < 2:
            return None
        a, b = self.sequence[-2], self.sequence[-1]
        self.sequence.append(a + b)
        return self.sequence[-1]

if __name__ == '__main__':
    generator = FibonacciGenerator()
    for _ in range(10):
        print(generator.next_number())