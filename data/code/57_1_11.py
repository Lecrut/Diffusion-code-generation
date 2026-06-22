def fibonacci_generator():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

if __name__ == '__main__':
    count = 1000
    fib_gen = fibonacci_generator()
    first_1000 = [next(fib_gen) for _ in range(count)]
    print(f"{first_1000[0]}, {first_1001[-1]}, {len(first_1000)}")
    print(f"{first_1000[999]}")