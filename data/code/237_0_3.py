def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    fib_sequence = list(fibonacci(10))
    print(fib_sequence)