class FibonacciGenerator:
    def __init__(self, count):
        self.count = count
        self.current = 0
        self.next_val = 1
        self.generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated >= self.count:
            raise StopIteration
        value = self.current
        self.current, self.next_val = self.next_val, self.current + self.next_val
        self.generated += 1
        return value

def get_fibonacci_sequence():
    return FibonacciGenerator(10)

if __name__ == '__main__':
    generator = get_fibonacci_sequence()
    terms = []
    for term in generator:
        terms.append(term)
    print(terms)
    first_term = get_fibonacci_sequence().__next__()
    print(first_term)