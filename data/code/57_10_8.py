def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    terms = list(fibonacci_generator(10))
    print(terms)