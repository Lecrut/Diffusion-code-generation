def generate_fibonacci(count):
    a, b = 0, 1
    n = 0
    while n < count:
        yield a
        a, b = b, a + b
        n += 1

if __name__ == '__main__':
    fib_gen = generate_fibonacci(1000)
    results = []
    while len(results) < 10:
        results.append(next(fib_gen))
    print(results)