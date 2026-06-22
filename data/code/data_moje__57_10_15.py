def fibonacci_generator(n=10):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    result = list(fibonacci_generator(10))
    print(result)