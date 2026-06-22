class FibonacciGenerator:
    def __init__(self):
        self.sequence = [1, 2]

    def next_number(self):
        if len(self.sequence) < 2:
            return self.sequence[-1]
        else:
            next_value = self.sequence[-1] + self.sequence[-2]
            self.sequence.append(next_value)
            return next_value

if __name__ == '__main__':
    generator = FibonacciGenerator()
    for _ in range(10):
        print(generator.next_number())