class FibonacciSequence:
    def __init__(self, count):
        self.count = count
        self.a = 0
        self.b = 1
        self.generated = 0

    def next_term(self):
        if self.generated >= self.count:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.generated += 1
        return value

    def get_all_terms(self):
        self.a = 0
        self.b = 1
        self.generated = 0
        terms = []
        for _ in range(self.count):
            terms.append(self.next_term())
        return terms

    def current_state(self):
        return (self.generated, self.a, self.b)

def fibonacci_generator(count=10):
    seq = FibonacciSequence(count)
    return seq.get_all_terms()

if __name__ == '__main__':
    sequence_obj = FibonacciSequence(10)
    first_term = sequence_obj.next_term()
    second_term = sequence_obj.next_term()
    print(first_term)
    print(second_term)
    print(sequence_obj.current_state())
    print(fibonacci_generator())