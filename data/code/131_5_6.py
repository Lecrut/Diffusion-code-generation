def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    max_limit = 100
    print(list(fibonacci_generator(max_limit)))