def fibonacci_generator(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    result = list(fibonacci_generator(10))
    print(result)