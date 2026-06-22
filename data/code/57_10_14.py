class FibonacciStream:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
        self.a = 0
        self.b = 1

    def generate(self):
        count = 0
        while count < self.limit:
            yield self.a
            self.a, self.b = self.b, self.a + self.b
            count += 1

    def get_last(self):
        return self.b

def run_fibonacci_stream():
    stream = FibonacciStream(10)
    result = list(stream.generate())
    last_val = stream.get_last()
    print(result)
    print(last_val)

if __name__ == '__main__':
    run_fibonacci_stream()