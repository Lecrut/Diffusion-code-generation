class FibonacciGenerator:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current

if __name__ == '__main__':
    generator = FibonacciGenerator(10)
    for num in generator:
        print(num)