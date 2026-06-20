def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    max_limit = 50
    for fib_num in fibonacci_generator(max_limit):
        print(fib_num)