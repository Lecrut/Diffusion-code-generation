def fibonacci_generator():
    count = 0
    a, b = 0, 1
    while count < 1000:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == '__main__':
    fib_gen = fibonacci_generator()
    first_ten = [next(fib_gen) for _ in range(10)]
    print(first_ten)
    print(next(fib_gen))