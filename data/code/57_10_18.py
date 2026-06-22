def create_fibonacci_generator(count):
    if not isinstance(count, int) or count < 0:
        raise ValueError("Count must be a non-negative integer")
    def _gen():
        a, b = 0, 1
        for _ in range(count):
            yield a
            a, b = b, a + b
    return _gen()

if __name__ == '__main__':
    fib_terms = create_fibonacci_generator(10)
    for term in fib_terms:
        print(term)