def fibonacci_generator(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    fib_numbers = list(fibonacci_generator(1000))
    print(fib_numbers[:10])
    print(fib_numbers[-1])