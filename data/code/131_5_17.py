def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    max_limit = 50
    fib_sequence = list(fibonacci_generator(max_limit))
    print("Fibonacci sequence up to", max_limit, ":", fib_sequence)